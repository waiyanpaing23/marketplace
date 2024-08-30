from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Username',
        'class' : ' w-100 py-2 px-3 rounded shadow-sm border-0'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Password',
        'class' : ' w-100 py-2 px-3 rounded shadow-sm border-0'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Username',
        'class' : ' w-100 py-2 px-3 rounded shadow-sm border-0'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Email Address',
        'class' : ' w-100 py-2 px-3 rounded shadow-sm border-0'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Password',
        'class' : ' w-100 py-2 px-3 rounded shadow-sm border-0'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password',
        'class' : ' w-100 py-2 px-3 rounded shadow-sm border-0'
    }))