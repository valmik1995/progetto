from dal import autocomplete
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from notizia.models import Notizia, News, Country
from notizia.validators import FileMimeValidator, FileMimeValidatorVideo

# 1. Definiamo un widget che supporti esplicitamente i file multipli
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class NotiziaForm(forms.ModelForm):
    class Meta:
        model = Notizia
        fields = ['title','tags', 'description','comune', 'date']
        widgets = {
            'date': DatePickerInput(format='%d/%m/%Y'),
        }

class NotiziaFullForm(NotiziaForm):
    # 2. Usiamo il nuovo widget MultipleFileInput qui
    images = forms.FileField(
        widget=MultipleFileInput(attrs={'multiple': True}),
        required=False
    )
    
    video = forms.FileField(
        widget=MultipleFileInput(attrs={'multiple': True}), 
        validators=[FileMimeValidatorVideo()], 
        required=False
    )

    # Spostiamo i widget nel Meta per coerenza Django
    class Meta(NotiziaForm.Meta):
        fields = NotiziaForm.Meta.fields + ['images', 'video']
        widgets = {
            **NotiziaForm.Meta.widgets,
            'comune': autocomplete.ModelSelect2(
                url='comune-autocomplete',
                attrs={'theme': 'bootstrap'}
            ),
        }

class NewsForm(forms.ModelForm):
    # 3. Applichiamo lo stesso widget anche qui
    files = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}))

    class Meta:
        model = News
        fields = ['title','description','files']
