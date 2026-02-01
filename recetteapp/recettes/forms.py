from django import forms
from .models import Recette

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['montant', 'immatriculation', 'nom_chauffeur', 'note', 'date_recette']
        widgets = {
            'montant': forms.NumberInput(attrs={'class': 'block w-full px-4 py-3 rounded-lg border-gray-200 focus:ring-blue-500 focus:border-blue-500 bg-gray-50','placeholder': 'Montant de la recette'}),
            'nom_chauffeur': forms.TextInput(attrs={'class': 'block w-full px-4 py-3 rounded-lg border-gray-200 focus:ring-blue-500 focus:border-blue-500 bg-gray-50', 'placeholder': 'Nom complet'}),
            'immatriculation': forms.TextInput(attrs={'class': 'block w-full px-4 py-3 rounded-lg border-gray-200 focus:ring-blue-500 focus:border-blue-500 bg-gray-50','placeholder': 'Matricule du véhicule'}),
            'date_recette': forms.DateInput(attrs={'type': 'date', 'class': 'block w-full px-4 py-3 rounded-lg border-gray-200 focus:ring-blue-500 focus:border-blue-500 bg-gray-50'}),
            'note': forms.Textarea(attrs={'rows': 3, 'class': 'block w-full px-4 py-3 rounded-lg border-gray-200 focus:ring-blue-500 focus:border-blue-500 bg-gray-50'}),
        }