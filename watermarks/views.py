from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect

from watermarks.forms import PhotoForm
from watermarks.models import Photo
from watermarks.services import create_photo_with_watermark



class BasicUploadView(CreateView):
    form_class = PhotoForm
    template_name = 'watermarks/uploads/uploads_task.html'
    success_url = reverse_lazy('watermarks:basic_upload')

    def get(self, request):
        form = PhotoForm()
        photos_list = Photo.objects.all()
        return render(self.request, self.template_name, {'photos': photos_list, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            try:
                for file in self.request.FILES.getlist('file'):
                    create_photo_with_watermark(file)
            except Exception as exc:
                form.add_error('file', str(exc))
                return render(request, self.template_name, {'form': form, 'photos': Photo.objects.all()})
            return redirect('watermarks:basic_upload')
        return render(request, self.template_name, {'form': form, 'photos': Photo.objects.all()})

def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.file_watermark.delete()
        photo.delete()

    return redirect(request.POST.get('next'))

def clear_database_heic(request):
    return clear_database(request)
