from django.urls import path, re_path, include # Rimosso from django.conf.urls import url
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notizia', views.NotiziaView)

app_name = 'notizia'

urlpatterns = [
    path('search/', views.search, name='notizia_search'),
    path('rest-framework/', include(router.urls)),
    path('create/', NotiziaCreateView.as_view(), name='notizia_create'),
    path('list/', NotiziaListView.as_view(), name='notizia_list'),
    path('<regione>/', NotiziaListViewRegione.as_view(), name='notizia_list_regione'),
    path('<regione>/<provincia>/', NotiziaListViewProvincia.as_view(), name='notizia_list_provincia'),
    path('<regione>/<provincia>/<comune>/', NotiziaListViewComune.as_view(), name='notizia_list_comune'),
    path('<int:pk>/', NotiziaDetailView.as_view(), name='notizia_detail'),
    path('<int:pk>/update/', NotiziaUpdateView.as_view(), name='notizia_update'),
    path('<int:pk>/delete/', ImagesDeleteView, name='images_delete'),
    path('ajax-posting/', ajax_posting, name='ajax_posting'),
    path('comune/', ComuneAutocomplete.as_view(), name='comune-autocomplete'),
]
