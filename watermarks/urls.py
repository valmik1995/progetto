from django.urls import re_path  # Sostituito django.conf.urls import url
from . import views

app_name = 'watermarks'

urlpatterns = [
    re_path(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    re_path(r'^basic-upload-heic/$', views.BasicUploadView.as_view(), name='basic_upload_heic'),
    re_path(r'^clear/$', views.clear_database, name='clear_database'),
    re_path(r'^clear_heic/$', views.clear_database_heic, name='clear_database_heic'),
]
