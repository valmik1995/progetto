from django import forms
from .models import Photo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
# Assicurati di importare i validatori correttamente se li usi
# from watermarks.validators import FileMimeValidator 

class PhotoForm(forms.ModelForm):
    file = forms.FileField(
        # Rimuoviamo 'multiple' da qui per evitare il ValueError all'avvio
        widget=forms.FileInput(attrs={'accept': 'image/*'}),
        label="Seleziona Immagini"
    )

    class Meta:
        model = Photo
        fields = ('file', )

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        
        # AGGIUNTA DINAMICA: Iniettiamo 'multiple' dopo che il widget è stato creato
        self.fields['file'].widget.attrs.update({
            'multiple': True,
            'value': 'Select Photo'
        })
        
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        # Obbligatorio per l'upload di file
        self.helper.form_enctype = 'multipart/form-data' 
        self.helper.layout = Layout(
            "file",
            Submit("submit", "Upload Files", css_class="btn btn-primary")
        )
