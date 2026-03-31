from __future__ import unicode_literals
import os
import json
import pdb
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django_celery_results.models import TaskResult
from django.core.files.storage import default_storage
from django.views.generic.edit import FormView
from core.celery import app
from celery.result import AsyncResult
from .forms import CaricamentoForm, FileFieldForm, SharingForm
from .models import Caricamento
from .tasks import process_file

UPLOAD_PATH = getattr(settings, 'AJAXIMAGE_DIR', 'ajaximage/')

def CaricamentoFiles(request):
    cntx = {}
    if request.method == 'POST':
        form = CaricamentoForm(request.POST, request.FILES)
        if form.is_valid():
            file_ = form.cleaned_data['photos']
            image_types = ['image/png', 'image/jpg', 'image/jpeg', 'image/pjpeg', 'image/gif']
            if file_.content_type not in image_types:
                data = json.dumps({'errore': 'Formato Immagine non supportato.'})
                return HttpResponse(data, content_type="application/json", status=403)
            name = os.path.join(UPLOAD_PATH, file_.name)
            path = default_storage.save(name, file_)
            image_path = settings.MEDIA_ROOT + '/' + path
            task = process_file.delay(image_path)
            cntx['task_id'] = task.id
            return render(request, 'caricamento/caricamento.html', cntx)
        else:
            return render(request, 'caricamento/caricamento.html', {'form':form})
    else:

            form = CaricamentoForm()
            return render(request, 'caricamento/caricamento.html', {'form': form})

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


def save_uploaded_file_to_media_root(f):
    with open('%s%s' % (settings.MEDIA_ROOT,f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def Index(request):
    if request.method == 'POST':
        form = SharingForm(request.POST, request.FILES)
        if form.is_valid():
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    save_uploaded_file_to_media_root(formfile)
            return HttpResponseRedirect('caricamento/uploads')
    else:
        form = SharingForm()
    return render(request,'caricamento/index.html',{'form':form})

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'caricamento/upload.html'  # Replace with your template.
    success_url = '../files/'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                 with open('/home/adirimini/Django_' + f.name, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def SostituzioneLettereFiles(request):
    if request.method == 'POST':
        form = SostituzioneForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            for path, dirs, files in os.walk(post.percorso):
                for name in files:
                    if(post.vecchia.lower() in name.lower()):
                        file_path = os.path.join(path, name)
                        new_name = os.path.join(path,name.lower().replace(post.vecchia,post.nuova))
                        os.rename(file_path, new_name)
            messages.success(request, 'Files Rinominati.')
            return render(request, 'caricamento/rinomina.html', {'form': form})
    else:
        form = SostituzioneForm()
        return render(request, 'caricamento/rinomina.html', {'form': form})
