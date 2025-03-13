from django import forms
from .models import Fichier

class FichierForm(forms.ModelForm):
    class Meta:
        model = Fichier
        fields = ['nom', 'fichier']