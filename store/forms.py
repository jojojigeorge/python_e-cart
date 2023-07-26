
from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeHolder':'User name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeHolder':'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeHolder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeHolder':'Conform password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']