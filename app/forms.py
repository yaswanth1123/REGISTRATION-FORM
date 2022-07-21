from dataclasses import fields
from pyexpat import model
from socket import fromshare
from tkinter import Widget
from django import forms

from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        Widget={'password':forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']
        