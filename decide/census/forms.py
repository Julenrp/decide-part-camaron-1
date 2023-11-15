from django import forms

class CensusForm(forms.Form):
    census_id = forms.IntegerField(label="census_id")
    
