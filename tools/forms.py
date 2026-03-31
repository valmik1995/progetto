from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from crispy_forms.bootstrap import Field
from tools.models import QrCode

class QrCodeForm(forms.ModelForm):
    class Meta:
        model = QrCode
        fields = [
            'title',
            'percorso',
        ]

    def __init__(self, *args, **kwargs):
        super(QrCodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('title', placeholder='titolo', css_class="qrcode-class"),
            Field('percorso', placeholder='inserisci url', css_class="qrcode-class"),
            Div(
               Submit('submit', 'Crea QrCode', css_class='btn btn-default'),
               css_class='col-md-3 form-group',
            )
            )

class DownloadForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Enter video url' }), label=False)

