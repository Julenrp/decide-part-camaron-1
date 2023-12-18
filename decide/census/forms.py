from django import forms

class FormularioPeticion(forms.Form):

    nombre = forms.CharField(label="Username", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea, required=True)
