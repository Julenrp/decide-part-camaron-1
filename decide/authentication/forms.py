from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)