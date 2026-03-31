from django.urls import path # Rimosso l'import url non più esistente
from . import views
from .views import *

app_name = 'foto'

urlpatterns = [
    path('galleria/', GalleriaListView.as_view(), name='gallery'),
    path('galleria/<str:pk>/', views.viewPhoto, name='photo'),
    path('delete/<str:pk>/', GalleriaDeleteView.as_view(), name='delete'),
    path('update/<str:pk>/', GalleriaUpdateView.as_view(), name='update'),
    path('aggiungi/', GalleriaCreateView.as_view(), name='add'),
    path('thumbails/', views.HomeView.as_view(), name='thumbails'),
    path('task/<str:task_id>/', views.TaskView.as_view(), name='task'),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
    path('search/', GalleriaElasticSearch.as_view(), name='search'),
    path('post-downloaded/', views.post_downloaded, name='postdownload'),
    
    # Fondamentale per la barra di progresso della galleria
    path('get-task-info/', GetTaskInfo, name='galleria_get_task_info'),
    
    path('download/', DownloadListViews.as_view(), name='download'),
    path('export/', export, name='export'),
]
