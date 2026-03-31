from django.urls import path, re_path  # Import corretti per Django 4/5
from . import views

app_name = 'caricamento'

urlpatterns = [
    re_path(r'^caricamento/uploads/$', views.CaricamentoFiles, name="uploads_files"),
    path('caricamento/files/', views.FileFieldView.as_view(), name='upload_files'),
    re_path(r'^caricamento/get-task-info/$', views.GetTaskInfo, name="get_task_info"),
    re_path(r'^rinomina/$', views.SostituzioneLettereFiles, name="sostituzione_lettere"),
    re_path(r'^caricamento/index/$', views.Index, name="upload_index"),
]
