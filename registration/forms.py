from django import forms
from django.core.exceptions import ValidationError

from .models import User


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Parollar bir xil emas')
        return self.cleaned_data['confirm_password']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))


class UpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']


class AboutForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'last_login', 'date_joined']
