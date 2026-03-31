from django.contrib import admin
from django.urls import path, re_path, include  # Import pulito e corretto
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Sostituito url() con re_path() per compatibilità regex
    re_path(r'^', include('caricamento.urls')),
    re_path(r'^', include('watermarks.urls')),
    
    path('video/', include('video.urls')),
    path('accounts/', include('accounts.urls')),
    path('notizia/', include('notizia.urls')),
    path('social/', include('social.urls')),
    path('tools/', include('tools.urls')),
    path('foto/', include('foto.urls')),
    
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/templates/favicon.ico'))),

    # Login and Logout
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='accounts/commons/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # REDIRECT HOME
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

# Se hai file media (video/immagini) in locale, aggiungi questo in fondo:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
