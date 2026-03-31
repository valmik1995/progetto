import os
import yt_dlp as youtube_dl
import yt_dlp
import re
import json
from requests import get
from math import pow, floor, log
from datetime import timedelta
from math import pow, floor, log
from django.conf import settings
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.template.defaultfilters import filesizeformat
from celery.result import AsyncResult
from .models import QrCode
from .tasks import video_copy
from .forms import QrCodeForm, DownloadForm

# Create your views here.

class QrCodeCreateView(CreateView):
    model = QrCode
    form_class = QrCodeForm
    template_name = 'tools/qrcode_form.html'
    success_url = '/tools/list/'

    def get(self, request):
        form = QrCodeForm()
        qrcode = QrCode.objects.all()
        return render(self.request, self.template_name, {'qrcode': qrcode, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save(commit=False)
            return super().form_valid(form)
        else:
            return render(request, self.template_name, {'form': form})

class QrCodeListView(ListView):
    template_name = 'tools/qrcode_list.html'
    queryset = QrCode.objects.all().order_by('-id')

class QrCodeDetailView(DetailView):
    template_name = 'tools/qrcode_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(QrCode, id=id_)

class QrCodeDeleteView(DeleteView):
    model=QrCode
    template_name = 'tools/qrcode_delete.html'
    success_url = '/tools/list/'


def download_video(request):
    global context
    form = DownloadForm(request.POST or None)

    if form.is_valid():
        video_url = form.cleaned_data.get("url")
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
        if not re.match(regex, video_url):
            return HttpResponse('Enter correct url.')

        ydl_opts = {}
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(
                    video_url, download=False)
            video_audio_streams = []
            for m in meta['formats']:
                file_size = m['filesize']
                if file_size is not None:
                    file_size = f'{round(int(file_size) / 1000000,2)} mb'

                resolution = 'Audio'
                if m['height'] is not None:
                    resolution = f"{m['width']}x{m['height']}"
                video_audio_streams.append({
                    'resolution': resolution,
                    'extension': m['ext'],
                    'file_size': file_size,
                    'video_url': m['url']
                })
            video_audio_streams = video_audio_streams[::-1]
            context = {
                'form': form,
                'title': meta.get('title', None),
                'streams': video_audio_streams,
                'description': meta.get('description'),
                'likes': f'{int(meta.get("like_count", 0)):,}',
                'dislikes': f'{int(meta.get("dislike_count", 0)):,}',
                'thumb': meta.get('thumbnails')[3]['url'],
                'duration': round(int(meta.get('duration', 1))/60, 2),
                'views': f'{int(meta.get("view_count")):,}'
            }
            return render(request, 'tools/youtube.html', context)
        except Exception as error:
            return HttpResponse(error.args[0])
    return render(request, 'tools/youtube.html', {'form': form})

def download_video_copy(request):

    if request.method == 'POST':
        cntx = {}
        # get link from the html form
        link = request.POST['link']
        task = video_copy.delay(link)
        cntx['task_id'] = task.id
        return render(request, 'tools/youtube-copy.html', cntx)

    return render(request, 'tools/youtube-copy.html')



def GetTaskInfo(request):
    task_id = request.GET.get('task_id', None)
    if task_id is not None:
        task = AsyncResult(task_id)
        data = {
            'state': task.state,
            'result': task.result,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse('No job id given.')

def yt_download(request):
    path = os.path.join(settings.MEDIA_ROOT) + '/youtube'
    files = os.listdir(path)
    filenames = files
    return render(request, 'tools/youtube-list.html', {'filenames': filenames})


def FilterData(ctx):
    title = ctx["title"]
    thumbnail = ctx["thumbnail"]
    formats = ctx["formats"]
    duration = str(timedelta(seconds = ctx["duration"]))
    description = ctx["description"]
    videosFormat = [f for f in formats if (f["vcodec"] != "none" and f["acodec"] != "none")]
    audiosFormat = [f for f in formats if (f["vcodec"] == "none" and f["acodec"] != "none")]
    videosFormatFiltered = []
    audiosFormatFiltered = []
    for v in videosFormat:
        a = dict()
        a["filesize"] = v["filesize"] if v["filesize"] != None else v["filesize_approx"]
        a['filesize'] = str(round((int(a['filesize'])/1024/1024), 1)) + "MB"
        a["url"] = v["url"]
        a["resolution"] = v["resolution"].split("x")[1]
        a["ext"] = v["ext"]
        videosFormatFiltered.append(a)
    for v in audiosFormat:
        a = dict()
        a["filesize"] = v["filesize"] if v["filesize"] != None else v["filesize_approx"]
        a['filesize'] = str(round((int(a['filesize'])/1024/1024), 1)) + "MB"
        a["url"] = v["url"]
        a["ext"] = v["ext"]
        a["abr"] = v["abr"]
        a["abr"] = str(int(a["abr"])) + "Kbps"
        audiosFormatFiltered.append(a)
    return {'title': title, 'duration': duration, 'thumbnail': thumbnail, 'description': description, 'videos': videosFormatFiltered, 'audios': audiosFormatFiltered, }



def GetDownloadOptions(request):
    ydl_opts = {}
    info = ""
    baseData = ""
    form = DownloadForm(request.POST or None)
    if form.is_valid():

        url = form.cleaned_data.get("url")
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
        if not re.match(regex, url):
            return HttpResponse('Enter correct url.')
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            baseData = FilterData(info)
        print(baseData)
        return render(request, 'tools/youtube.html', baseData)

    return render(request, 'tools/youtube.html', {'form': form}) 

