from django.forms import ModelForm
from django import forms
from caricamento.models import Caricamento

# 1. Definiamo il widget personalizzato per supportare i file multipli
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class CaricamentoForm(ModelForm):
    class Meta:
        model = Caricamento
        fields = ['photos',]

class FileFieldForm(forms.Form):
    # 2. Sostituiamo il widget standard con quello personalizzato
    file_field = forms.FileField(
        widget=MultipleFileInput(attrs={'multiple': True})
    )

class SharingForm(forms.Form):
    video = forms.FileField()
    # 3. Applichiamo la modifica anche qui
    photo = forms.FileField(
        widget=MultipleFileInput(attrs={'multiple': True})
    )
