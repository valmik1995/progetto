import time
import os
import json
from subprocess import Popen, PIPE, STDOUT
from django.conf import settings
from django import forms
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from core.celery import app
from django_celery_results.models import TaskResult
from celery.result import AsyncResult
from celery import current_app
from taggit.models import Tag
from foto.tasks import watermarks, make_thumbnails
from foto.forms import GalleriaForm
from foto.models import Categoria, Galleria, Download
from foto.resources import GalleriaResource
from django.contrib.auth.mixins import LoginRequiredMixin
from elasticsearch_dsl import Q, Search  # Pulizia import ES
from .templatetags import auth_extras

# --- FIX: Definizione del widget per file multipli ---
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

# --- FIX: FileUploadForm spostato qui per risolvere il ValueError ---
class FileUploadForm(forms.Form):
    image_file = forms.ImageField(
        widget=MultipleFileInput(attrs={'multiple': True}), 
        required=True
    )

@login_required
def gallery(request):
    category = request.GET.get('category')
    if category is None:
        photos = Galleria.objects.all()
    else:
        photos = Galleria.objects.filter(category__name=category)

    categories = Categoria.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'foto/galleria/galleria.html', context)

class GalleriaListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Galleria
    template_name = 'foto/galleria/galleria.html'
    paginate_by = 15
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Categoria.objects.all().order_by('name')
        return context

    def get_queryset(self):
        queryset = Galleria.objects.all().order_by('-id')
        category = self.request.GET.get('category', None)
        titolo = self.request.GET.get('titolo', None)
        if category:
            queryset = queryset.filter(category__name=category)
        elif titolo:
            queryset = queryset.filter(title=titolo)
        return queryset

class GalleriaDeleteView(DeleteView):
    model = Galleria
    template_name = 'foto/galleria/delete.html'
    success_url = reverse_lazy('foto:gallery')

class GalleriaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Galleria
    form_class = GalleriaForm
    template_name = 'foto/galleria/update.html'
    success_url = reverse_lazy('foto:gallery')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GalleriaCreateView(CreateView):
    form_class = GalleriaForm
    template_name = 'foto/galleria/aggiungi.html'
    success_url = reverse_lazy('foto:gallery')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        cntx = {}
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = self.request.user
            data = self.request.POST
            task_ids = []
            
            # Gestione upload multiplo
            files = request.FILES.getlist('image')
            for image in files:
                photo = Galleria.objects.create(
                    category=form.cleaned_data['category'],
                    user=request.user,
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    image=image,
                    date=form.cleaned_data['date'],
                    # gruppo=form.cleaned_data['gruppo'] # Se gestito come ManyToMany
                )
                
                # Salvataggio Tag
                tags_list = data.get('tags', '').lower().split(",")
                for tag in tags_list:
                    if tag.strip():
                        photo.tags.add(auth_extras.upper_tags(tag.strip()))
                
                task_ids.append(photo.id)
            
            # Avvio task Celery per i watermark
            if task_ids:
                task = watermarks.delay(task_ids)
                cntx['task_id'] = task.id
            
            return render(request, 'foto/galleria/aggiungi.html', cntx)
        else:
            return render(request, self.template_name, {'form': form})

class HomeView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, 'foto/thumbails.html', {'form': form})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            # Assicurati che IMAGES_DIR esista
            if not os.path.exists(settings.IMAGES_DIR):
                os.makedirs(settings.IMAGES_DIR)
                
            file_obj = request.FILES['image_file']
            file_path = os.path.join(settings.IMAGES_DIR, file_obj.name)
            
            with open(file_path, 'wb+') as fp:
                for chunk in file_obj.chunks():
                    fp.write(chunk)
            
            task = make_thumbnails.delay(file_path, thumbnails=[(128, 128)])
            context['task_id'] = task.id
            context['task_status'] = task.status
            return render(request, 'foto/thumbails.html', context)
        
        context['form'] = form
        return render(request, 'foto/thumbails.html', context)

class TaskView(View):
    def get(self, request, task_id):
        task = AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}
        if task.status == 'SUCCESS':
            response_data['results'] = task.get()
        return JsonResponse(response_data)

def GetTaskInfo(request):
    task_id = request.GET.get('task_id', None)
    if task_id:
        task = AsyncResult(task_id)
        data = {
            'state': task.state,
            'result': str(task.result) if task.failed() else task.result,
        }
        return JsonResponse(data)
    return HttpResponse('No job id given.', status=400)

# --- (Le altre funzioni addPhoto, tagged, viewPhoto rimangono simili ma ottimizzate) ---

def viewPhoto(request, pk):
    photo = get_object_or_404(Galleria, id=pk)
    # Importante: exiftool deve essere installato sul sistema
    filename = os.path.join(settings.MEDIA_ROOT, str(photo.image))
    process = Popen(['exiftool', filename], stdout=PIPE, stderr=STDOUT)
    output_byte = process.stdout.read()
    output_list = output_byte.decode('utf-8', errors='ignore').split('\n')
    return render(request, 'foto/galleria/foto.html', {'photo': photo, "output": output_list})

class GalleriaElasticSearch(LoginRequiredMixin, ListView):
    template_name = 'foto/search/results_foto.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q')
        context['category'] = Categoria.objects.all().order_by('name')
        return context

    def get_queryset(self):
        search_term = self.request.GET.get('q', None)
        if search_term:
            q = Q("multi_match", query=search_term, fields=['description', 'title'], operator='AND') | \
                Q("match", tags__name=search_term)
            s = Search().query(q)
            return s.execute()
        return Galleria.objects.order_by('-id')

def post_downloaded(request):
    photo_id = request.GET.get('q')
    if photo_id:
        Download.objects.create(user=request.user, content_object_id=int(photo_id))
    return JsonResponse({'status': 'ok'})

class DownloadListViews(ListView):
    model = Download
    template_name = 'foto/download_list.html'
    paginate_by = 16

def export(request):
    person_resource = GalleriaResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="galleria.csv"'
    return response


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    categories = Categoria.objects.all().order_by('name')
    photos = Galleria.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'photos': photos,
        'category': categories
    }
    return render(request, 'foto/galleria/tags.html', context)
