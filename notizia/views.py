from __future__ import unicode_literals
import json
import pdb
from dal import autocomplete
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, Http404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from core.celery import app
from django_celery_results.models import TaskResult
from celery.result import AsyncResult
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from notizia.forms import NotiziaForm, NotiziaFullForm
from notizia.models import Notizia, Images, Country, VideoNotizia, Comune, Provincia, Regione
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from dal import autocomplete
from rest_framework import viewsets
from .serializers import NotiziaSerializer
from taggit.models import Tag

class NotiziaView(viewsets.ModelViewSet):
    queryset = Notizia.objects.all()
    serializer_class = NotiziaSerializer

class ComuneAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Comune.objects.none()

        qs = Comune.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class HomePageView(TemplateView):
    template_name = "notizia/notizia_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Notizia.objects.all().order_by('id')
        return context


@csrf_exempt
def more_todo(request):
    if request.is_ajax():
        todo_items = ['Valerio Podrini', 'Michela D\'Arcangelo',]
        data = json.dumps(todo_items)
        return HttpResponse (data, content_type = 'application/json')
    else:
        raise Http404

@csrf_exempt
def add_todo(request):
    if request.is_ajax() and request.POST:
        data = {'message': "%s added" % request.POST.get('item')}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404


# def notizia_update(request, pk, template_name='notizia/notizia_form_autocomplete.html'):
#     if request.user.is_superuser:
#         notizia= get_object_or_404(Notizia, pk=pk)
#     else:
#         notizia= get_object_or_404(Notizia, pk=pk, user=request.user)
#     form = NotiziaFullForm(request.POST or None, request.FILES or None, instance=notizia)
#     if form.is_valid():
#         form.save()
#         return redirect('notizia:notizia_list')
#     return render(request, template_name, {'form':form})

class NotiziaUpdateView(UpdateView):
    model = Notizia
    template_name_suffix = '_update_form'
    form_class = NotiziaFullForm



class NotiziaCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': NotiziaFullForm()}
        return render(request, 'notizia/notizia_form_autocomplete.html', context)

    def post(self, request, *args, **kwargs):
        form = NotiziaFullForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        video = request.FILES.getlist('video')
        if form.is_valid():
            notizia = form.save()
            notizia.user = request.user
            notizia.save()
            for f in files:
                Images.objects.create(note_id=notizia.id,image=f)

            for v in video:
                VideoNotizia.objects.create(note_id=notizia.id,video=v)

            return HttpResponseRedirect(reverse_lazy('notizia:notizia_detail', args=[notizia.id]))
        return render(request, 'notizia/notizia_form_autocomplete.html', {'form': form})


# class CountryAutocompleteView(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         if not self.request.user.is_authenticated():
#             return Country.objects.none()
#
#         qs = Country.objects.all()
#
#         if self.q:
#             qs = qs.filter(name__icontains=self.q)
#
#         return qs
#

# def addNotiziaView(request):
#     posts = Notizia.objects.all()
#     response_data = {}
#     form = NotiziaFullForm(request.POST or None, request.FILES or None)
#     files = request.FILES.getlist('images')
#     if form.is_valid():
#         file_ = form.cleaned_data['images']
#         image_types = ['image/png', 'image/jpg', 'image/jpeg', 'image/gif', 'image/gif']
#         if file_.content_type not in image_types:
#             data = json.dumps({'errore': 'Formato Immagine non supportato.'})
#             return HttpResponse(data, content_type="application/json", status=403)
#         user = request.user
#         title = form.cleaned_data['title']
#         description = form.cleaned_data['description']
#         notizia_obj = Notizia.objects.create(user=user,title=title,description=description) #create will create as well as save too in db.
#         for f in files:
#             Images.objects.create(note=notizia_obj,image=f)
#         object = {"title": title, "description": description}
#         response_data['title'] = title
#         response_data['description'] = description
#         return HttpResponseRedirect('/notizia/list/')
#
#     return render(request, 'notizia/notizia_form_autocomplete.html', {'posts':posts})

# def addNotiziaView(request, *args, **kwargs):
#     posts = Notizia.objects.all()
#     response_data = {}
#
#     if request.POST.get('action') == 'post':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         files = request.FILES.get('image')
#         user = request.user
#
#
#
#         response_data['title'] = title
#         response_data['description'] = description
#
#         notizia_obj = Notizia.objects.create(user=user,title = title,description = description)
#
#         Images.objects.create(note=notizia_obj,image=files)
#         return JsonResponse(response_data)
#
#     return render(request, 'notizia/notizia_form.html', {'posts':posts})


class NotiziaListView(ListView):
    model = Notizia
    template_name = 'notizia/notizia_list.html'
    paginate_by = 10  # if pagination is desired
    ordering = ['-created_date']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class NotiziaDetailView(DetailView):
    model = Notizia
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class NotiziaListViewComune(ListView):
    template_name = 'notizia/notizia_list.html'

    def get_queryset(self):
        self.comune = get_object_or_404(Comune, name=self.kwargs['comune'])
        return Notizia.objects.filter(comune=self.comune)

class NotiziaListViewProvincia(ListView):
    template_name = 'notizia/notizia_list.html'

    def get_queryset(self):
        return Notizia.objects.filter(comune__provincia__name = self.kwargs['provincia'])

class NotiziaListViewRegione(ListView):
    template_name = 'notizia/notizia_list.html'

    def get_queryset(self):
        return Notizia.objects.filter(comune__provincia__regione__name = self.kwargs['regione'])


# class NotiziaDeleteView(DeleteView):
#     template_name = 'notizia/notizia_delete.html'
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Images, note_id=id_)
#
#     def get_success_url(self):
#         return reverse('notizia:notizia_list')

# class ImagesDeleteView(DeleteView):
#     template_name = 'notizia/notizia_delete.html'
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Images, id=id_)
#
#     def get_success_url(self):
#         return reverse('notizia:notizia_list')

def ImagesDeleteView(request, pk):
    query = Images.objects.filter(note_id=pk).delete()
    instance = Notizia.objects.get(id=pk)
    instance.delete()
    return HttpResponseRedirect(reverse_lazy('notizia:notizia_list'))



# ajax_posting function
@csrf_exempt
def ajax_posting(request):
    if request.is_ajax():
        first_name = request.POST.get('first_name', None) # getting data from input first_name id
        last_name = request.POST.get('last_name', None)  # getting data from input last_name id
        if first_name and last_name: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON

@csrf_exempt
def requestAjax(request):
    if request.is_ajax() and request.POST:
        data = {'message': "%s added" % request.POST.get('item')}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404


def search(request):
    q = request.GET.get('q')

    if q:
        notizia = NotiziaDocument.search().query("multi_match", query=q, fields=['title', 'description'])
    else:
        notizia = 'Nessun risultato'
    return render(request, 'notizia/search.html', {'notizia': notizia, 'text': q})
