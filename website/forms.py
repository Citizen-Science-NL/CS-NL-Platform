from django import forms
from .models import *

class Form(forms.ModelForm):
    class Meta:
        model = Hero
        fields = '__all__'
        widgets = {
            'title': form.TextInput(attrs={'class': 'form-control'})
        }