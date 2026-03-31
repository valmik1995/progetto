from django import forms
from django.contrib.auth.models import User
# CORREZIONE: Import specifico dal sotto-modulo widgets
from bootstrap_datepicker_plus.widgets import DatePickerInput 

class SearchForm(forms.Form):
    query = forms.CharField(label="Full-text Search Query", required=False)
    title = forms.CharField(label="Text", required=False)
    
    users = forms.ModelMultipleChoiceField(
        label="Users", 
        queryset=User.objects.all(), 
        required=False, 
        widget=forms.CheckboxSelectMultiple()
    )
    
    # CORREZIONE: Uso del dizionario 'options' per il formato data (standard Moment.js)
    published_from = forms.DateField(
        label="Published from", 
        required=False, 
        widget=DatePickerInput(options={
            "format": "DD/MM/YYYY",
        })
    )
    
    published_till = forms.DateField(
        label="Published till", 
        required=False, 
        widget=DatePickerInput(options={
            "format": "DD/MM/YYYY",
        })
    )
