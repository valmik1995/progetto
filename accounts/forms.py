from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from leaflet.forms.widgets import LeafletWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import FormActions

# Sign Up Form



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(
        max_length=254, help_text='Enter a valid email address')


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


# Profile Form
class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'qualifica',
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('comando', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'profile_pic',
            'geom',
            FormActions(Submit('submit', 'Sign in', css_class="col-md-12 btn-primary")),
        )
    class Meta:
        model = Profile
        fields = [
            'qualifica',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'comando',
            'profile_pic',
            'geom',
        ]
        widgets = {'geom': LeafletWidget()}


        
class ProfilePageForm(forms.ModelForm):
    model = Profile
    field = ('first_name')



class ContactForm(forms.Form):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email_address = forms.EmailField(max_length=150)
	message = forms.CharField(widget=forms.Textarea, max_length=2000)
