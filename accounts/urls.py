from django.urls import path
from . import views  # Importiamo l'intero modulo views
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import Profile
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # Usiamo views.NomeClasse per essere sicuri del riferimento
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
    path("profile_rest", views.ListCreateGenericViews.as_view()),
    path("profile_rest/<str:pk>", views.ProfileUpdateRetreiveView.as_view()),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', views.EditProfilePage.as_view(), name='edit_profile_page'),
    path('create_profile_page/', views.CreateProfilePageView.as_view(), name='create_profile_page'),
    path('data_geojson_coem/', GeoJSONLayerView.as_view(model=Profile, properties=('first_name', 'phone_number', 'last_name')), name='data_geojson_coem'),
    path('mappa_coem/', TemplateView.as_view(template_name='accounts/mappa_coem.html'), name='mappa_coem'),
    path('lista_coem/', views.EntryList.as_view(), name='lista_coem'),
    path("contact", views.contact, name="contact"),
]

# Estensione per Password Management
urlpatterns += [
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/commons/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/commons/password-reset/password_reset.html',
             subject_template_name='accounts/commons/password-reset/password_reset_subject.txt',
             email_template_name='accounts/commons/password-reset/password_reset_email.html',
             success_url='/accounts/password-reset/done/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/commons/password-reset/password_reset_confirm.html',
             success_url='/accounts/password-reset-complete/'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/commons/password-reset/password_reset_complete.html',
         ),
         name='password_reset_complete'),
]
