from django.urls import path, re_path  # Rimosso from django.conf.urls import url
from . import views
from .views import *

app_name = 'social'

urlpatterns = [
    # Usiamo re_path per mantenere la compatibilità con le regex r'^...'
    re_path(r'^db/$', views.tweet_fetch, name="save_to_Db"),
    
    path("tweet_set_inactive/<int:pk>/", views.tweet_set_inactive, name="tweet_set_inactive"),
    path("tweet_set_active/<int:pk>/", views.tweet_set_active, name="tweet_set_active"),
    
    # La home dell'app social (es. /social/)
    re_path(r'^$', CategoryElasticSearch.as_view(), name="twitter_search"),
    
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
