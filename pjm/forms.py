from django import forms
from pjm.models import ecoProject

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ecoProject
        fields = '__all__'
