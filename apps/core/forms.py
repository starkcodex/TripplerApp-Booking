from django.forms import ModelForm
from .models import *
from django import forms


class HolidayCreateForm(ModelForm):
    class Meta:
        model = Holiday
        fields =  ['url','body']
        labels = {
            'body': 'Caption',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows':3, 'placeholder': 'add a address','class': 'font text-4xl'}),
            'url' : forms.TextInput(attrs={'placeholder': 'Add url ...'}),
        }
