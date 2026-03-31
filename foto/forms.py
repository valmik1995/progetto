from django import forms
from django.contrib.auth.models import Group
from django.forms import Textarea
from foto.models import Galleria, Categoria
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
# CORREZIONE: Import specifico per il widget del calendario
from bootstrap_datepicker_plus.widgets import DatePickerInput

# 1. Definiamo il widget che abilita il supporto ai file multipli
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

# Funzione per recuperare i gruppi (mantenuta come l'originale)
def get_gruppo_choices():
    return tuple([(str(g.id), g.name) for g in Group.objects.all()])

class GalleriaForm(forms.ModelForm):
    # 2. Applichiamo il widget personalizzato per risolvere il ValueError
    image = forms.FileField(
        widget=MultipleFileInput(attrs={
            'multiple': True, 
            'accept': '.png, .jpg, .jpeg, .cr2, .nef'
        }),
        required=False
    )
    
    category = forms.ModelChoiceField(queryset=Categoria.objects.order_by('name'))
    
    gruppo = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=get_gruppo_choices()
    )

    class Meta:
        model = Galleria
        fields = ('title', 'description', 'date', 'tags', 'category', 'image', 'gruppo')
        widgets = {
            # CORREZIONE: Uso di 'options' per il formato data (standard Moment.js)
            'date': DatePickerInput(options={
                "format": "DD/MM/YYYY",
            }),
            "tags": forms.TextInput(attrs={"data-role": "tagsinput"}),
            'description': Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aggiorniamo le scelte dei gruppi ad ogni inizializzazione per evitare dati obsoleti
        self.fields['gruppo'].choices = get_gruppo_choices()
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # Rimuoviamo il pulsante di submit automatico se preferisci gestirlo nel template, 
        # o lo manteniamo come nel tuo originale:
        self.helper.add_input(Submit('submit', 'Save Photo'))
        
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('date', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('category', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('tags', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('description', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('gruppo', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
        )
