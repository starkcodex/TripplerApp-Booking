from django.forms import ModelForm
from .models import *
from django import forms


class HotelCreateForm(ModelForm):
    class Meta:
        model = Hotel
        fields =  '__all__'
        labels = {
            'address': 'Address Detail',
        }
        widgets = {
            'address': forms.Textarea(attrs={'rows':3, 'placeholder': 'add a address','class': 'font text-4xl'}),
        }


# class AddcategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'category']


# class UpdatecategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'category']
        
        
# class AddRoomForm(forms.ModelForm):
#     class Meta:
#         model = Room
#         fields = '__all__'
        
        
# class UpdateRoomForm(forms.ModelForm):
#     class Meta:
#         model = Room
#         fields = '__all__'