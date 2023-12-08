from django import forms

class FormularioPeticion(forms.Form):
    census_id = forms.IntegerField(label="census_id")
    