from django.urls import path, re_path  # Sostituito url con re_path
from .views import VideoCreateView, VideoDetailView, VideoListView, VideoUpdateView, VideoDeleteView, GetTaskInfo
from . import views

app_name = 'video'

urlpatterns = [
    path('list/', VideoListView.as_view(), name='video-list'),
    path('create/', VideoCreateView.as_view(), name='video-create'),
    path('<int:id>/', VideoDetailView.as_view(), name='video-detail'),
    path('update/<int:id>/', VideoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.VideoDeleteView.as_view(), name='delete'),
    path('get-task-info/', GetTaskInfo, name='video_get_task_info'),
    
    # Sostituito url() con re_path() per compatibilità
    re_path(r'^clear/$', views.clear_database, name='clear_database'),
]
