from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    password2 = forms.CharField(
        label="confirm password",
        widget=forms.PasswordInput,
        help_text="Re-enter password."
    )
    class Meta:
        model = User
        fields = ('phone_number', 'password', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone_number', 'password', 'is_active', 'is_staff')