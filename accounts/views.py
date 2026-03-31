import email
from django.contrib.messages.api import success
from django.conf import settings
from django.db import models
from django.utils.http import urlsafe_base64_decode
# CORREZIONE: force_str sostituisce force_text nelle versioni moderne di Django
from django.utils.encoding import force_bytes, force_str 
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View, UpdateView, DetailView, CreateView, ListView
from accounts.forms import SignUpForm, ProfileForm, ProfilePageForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from rest_framework import generics
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from accounts.models import Profile
from accounts.serializers import ProfileSerializer
from accounts.tokens import account_activation_token
from accounts.forms import ContactForm

# Configurazione geolocalizzatore
geolocator = Nominatim(user_agent="location")

# --- Sign Up View ---
class SignUpView(View):
    form_class = SignUpForm
    template_name = 'accounts/commons/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Account disattivato fino a conferma email
            user.save()

            current_site = get_current_site(request)
            subject = 'Attiva il tuo account sul nostro sito web'
            message = render_to_string('accounts/emails/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, 'Ti abbiamo inviato un\'email. Per favore, conferma la tua registrazione.')
            return redirect('home')

        return render(request, self.template_name, {'form': form})

# --- Activate Account ---
class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            # CORREZIONE: force_str per compatibilità Python 3.12
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            
            # Aggiorna il profilo se esiste
            Profile.objects.filter(user=user).update(signup_confirmation=True)
            
            login(request, user)
            messages.success(request, 'Il tuo account è stato confermato con successo!')
            return redirect('home')
        else:
            messages.warning(request, 'Il link di attivazione non è valido o è già stato utilizzato.')
            return redirect('home')

# --- Profile Views ---
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/commons/profile.html'

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/commons/profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # CORREZIONE: super().form_valid(form) per Django 4+
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:show_profile_page', kwargs={'pk': self.object.pk})

class EditProfilePage(generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/commons/profile.html'
    
    def get_success_url(self):
        return reverse_lazy('accounts:show_profile_page', kwargs={'pk': self.object.pk})

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'accounts/user.html'
    context_object_name = 'profile'

class EntryList(ListView):
    queryset = Profile.objects.filter(geom__isnull=False)

# --- API Views (REST Framework) ---
class ListCreateGenericViews(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        address = serializer.initial_data.get("address")
        if address:
            try:
                g = geolocator.geocode(address)
                if g:
                    pnt = Point(g.longitude, g.latitude)
                    serializer.save(location=pnt)
                else:
                    serializer.save()
            except:
                serializer.save()
        else:
            serializer.save()

class ProfileUpdateRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_update(self, serializer):
        address = serializer.initial_data.get("address")
        if address:
            try:
                g = geolocator.geocode(address)
                if g:
                    pnt = Point(g.longitude, g.latitude)
                    serializer.save(location=pnt)
                else:
                    serializer.save()
            except:
                serializer.save()
        else:
            serializer.save()

# --- Contact Form ---
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Nuovo messaggio dal sito web"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join([f"{k.capitalize()}: {v}" for k, v in body.items()])

            try:
                # settings.ADMINS è solitamente una lista di tuple (Nome, Email)
                admin_emails = [a[1] for a in settings.ADMINS] if settings.ADMINS else []
                send_mail(subject, message, body['email'], admin_emails)
                messages.success(request, 'Messaggio inviato con successo!')
            except Exception:
                messages.error(request, 'Si è verificato un errore nell\'invio del messaggio.')
            
            return redirect('home')

    form = ContactForm()
    return render(request, "accounts/contact_form.html", {'form': form})
