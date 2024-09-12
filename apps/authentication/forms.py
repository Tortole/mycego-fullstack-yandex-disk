"""
Module with forms for authentication app
"""

from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    """
    Form for registration new user by inner Django User model
    """

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {"password": forms.PasswordInput()}

    def save(self, commit: bool = True) -> User:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
