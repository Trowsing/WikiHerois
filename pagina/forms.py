from django import forms
from .models import Heroes

class HeroesForm(forms.ModelForm):
    class Meta:
        model = Heroes
        fields = ('name', 'description', 'image', )
