from django import forms
from video.models import Video


class VideoForm(forms.ModelForm):
    video = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'video/*'}))
    posizione = forms.ChoiceField(
        choices=(
            ('ORIZ', 'Orizzontale'),
            ('VERT', 'Verticale con bande'),
        ),
        widget=forms.RadioSelect,
        initial='ORIZ',
        label='Orientamento',
    )
    codino = forms.ChoiceField(
        choices=(
            ('CODIN', 'Con codino'),
            ('SENZA', 'Senza codino'),
        ),
        widget=forms.RadioSelect,
        initial='CODIN',
        label='Codino',
    )
    logo = forms.ChoiceField(
        choices=(
            ('LOGO', 'Con logo'),
            ('SENZ', 'Senza logo'),
        ),
        widget=forms.RadioSelect,
        initial='LOGO',
        label='Logo',
    )

    class Meta:
        model = Video
        fields = [
            'title',
            'formato',
            'posizione',
            'codino',
            'logo',
            'video'
        ]
