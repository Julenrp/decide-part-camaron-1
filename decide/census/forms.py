from django import forms
from .models import Census

class FormularioPeticion(forms.Form):

    inicial = Census.objects.all().first() if Census.objects.all().exists() else None

    census_name = forms.ModelChoiceField(queryset=Census.objects.all(), initial=inicial, label="Nombre del Censo")
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea, required=True)

