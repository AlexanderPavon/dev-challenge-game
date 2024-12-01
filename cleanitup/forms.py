from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Player

class PlayerRegistrationForm(UserCreationForm):
    """Formulario personalizado de registro"""
    email = forms.EmailField(required=False)

    class Meta:
        model = Player
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['email']:
            user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user