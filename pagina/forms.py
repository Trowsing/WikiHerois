from django import forms
from .models import Heroes

class HeroesForm(forms.ModelForm):

    class Meta:
        model = Heroes
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'nes-input', 'style':'width: 500px;'}),
            'description': forms.Textarea(attrs={'class': 'nes-textarea', 'style': 'width: 600px;'})
        }
