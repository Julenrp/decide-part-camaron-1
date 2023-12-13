from django import forms

class FormularioPeticion(forms.Form):

    census_id = forms.IntegerField(label="census_id")
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea, required=True)

