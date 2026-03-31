from django.views.generic import View, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoForm
from .models import Video
from .tasks import watermark

from django.http import JsonResponse
from core.celery import app as celery_app

class VideoCreateView(View):

    form_class = VideoForm
    success_url = reverse_lazy('video:video-list')
    template_name = 'video/progress.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_video = form.save()
            task = watermark.delay(new_video.pk)
            return render(
                request,
                self.template_name,
                {
                    'task_id': task.id,
                    'video_obj': new_video,
                },
            )
        return render(request, self.template_name, {'form': form})

class VideoDetailView(DetailView):
    template_name = 'video/video_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Video, id=id_)

class VideoListView(ListView):
    template_name = 'video/video_list.html'
    queryset = Video.objects.all().order_by('-id') # <blog>/<modelname>_list.html

class VideoUpdateView(UpdateView):
    template_name = 'video/progress.html'
    form_class = VideoForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Video, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# class VideoDeleteView(DeleteView):
#     template_name = 'video/video_delete.html'
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Video, id=id_)
#
#     def get_success_url(self):
#         return reverse('video:video-list')

def GetTaskInfo(request):
    task_id = request.GET.get('task_id', None)
    video_id = request.GET.get('video_id')
    if not task_id:
        return JsonResponse({'error': 'No job id given.'}, status=400)

    task = celery_app.AsyncResult(task_id)
    task_meta = task.info if isinstance(task.info, dict) else {}
    response_data = {
        'state': task.state,
        'result': None,
        'status': None,
    }
    if task.state == 'FAILURE':
        response_data['status'] = str(task.result)
    elif task.state == 'SUCCESS':
        response_data['result'] = task.result
    elif task.state == 'STARTED':
        response_data.update({'percent': task_meta.get('percent', 30), 'status': task_meta.get('status', 'Elaborazione in corso...')})
    elif task.state == 'PROGRESS':
        response_data.update(task_meta)
    elif task.state == 'PENDING' and video_id:
        video_obj = Video.objects.filter(pk=video_id).only('video_watermarks').first()
        if video_obj and video_obj.video_watermarks:
            response_data = {
                'state': 'SUCCESS',
                'result': {'status': 'SUCCESS'},
                'status': 'Completato.',
            }
    return JsonResponse(response_data)


def video_delete_view(request, id):
    obj = get_object_or_404(Video, id=id)
    if request.method == "POST":
        obj.video.delete()
        obj.video_watermarks.delete()
        obj.delete()
        return redirect('../../list')
    context = {
    "object": obj
    }
    return render(request, "video/video_delete.html", context)

class VideoDeleteView(DeleteView):
    model=Video
    template_name='video/video_delete.html'
    success_url = '/video/list/'

def clear_database(request):
    for video in Video.objects.all():
        video.video.delete()
        video.video_watermarks.delete()
        video.delete()
    return redirect('../create')


#def page_not_found_view(request, exception):
#    return render(request, '404.html', status=404)


