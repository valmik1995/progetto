from django.urls import path  # Rimosso l'import di url (non più supportato)
from . import views

app_name = 'tools'

urlpatterns = [
    path('qrcode/', views.QrCodeCreateView.as_view(), name='create'),
    path('list/', views.QrCodeListView.as_view(), name='list'),
    path('<int:id>/', views.QrCodeDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.QrCodeDeleteView.as_view(), name='delete'),
    
    path('download/', views.GetDownloadOptions, name='detail-download'),
    path('download_copy/', views.download_video_copy, name='detail-download-copy'),
    path('download_list/', views.yt_download, name='detail-download-list'),
    
    # Questa rotta è vitale per la barra di progresso dei tools
    path('get-task-info/', views.GetTaskInfo, name='get_task_info'),
]
