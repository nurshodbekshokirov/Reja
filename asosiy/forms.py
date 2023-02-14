from django import forms
from .models import *

class RejaForm(forms.ModelForm):
    class Meta:
        model = Reja
        fields = ('sarlavha', 'vaqt', 'batafsil',  'holat')
