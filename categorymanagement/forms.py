from django import forms
from .models import *

class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name','description']