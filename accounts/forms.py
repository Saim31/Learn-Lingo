from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg rounded-pill px-4 py-3 shadow-sm',
        'placeholder': 'Enter your first name',
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg rounded-pill px-4 py-3 shadow-sm',
        'placeholder': 'Enter your last name',
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg rounded-pill px-4 py-3 shadow-sm',
        'placeholder': 'Enter your email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg rounded-pill px-4 py-3 shadow-sm',
        'placeholder': 'Enter your username',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg rounded-pill px-4 py-3 shadow-sm',
        'placeholder': 'Enter your password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg rounded-pill px-4 py-3 shadow-sm',
        'placeholder': 'Re-enter your password',
    }))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
