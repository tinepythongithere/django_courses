from django import forms
from .models import QuestionnaireEnergie

class QuestionnaireEnergieForm(forms.ModelForm):
    class Meta:
        model = QuestionnaireEnergie
        fields = ['organisation_loue', 'achat_electricite', 'surface_climatisee',
                  'nombre_employes_dechet', 'nombre_employes_eau', 'cout_renovation']