from django import forms
from .models import WordCard

class WordCardForm(forms.ModelForm):
    class Meta:
        model = WordCard
        fields = ['word', 'translation', 'image']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
        }