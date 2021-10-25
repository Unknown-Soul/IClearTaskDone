from django import forms
from .models import IP, MyUser
from django.contrib.auth.forms import UserCreationForm


class IP(forms.ModelForm):
    class Meta:
        model = IP
        fields = ('ip','hour','minute','second')


class UserRegistration(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('email','first_name', 'last_name', 'dateOfBirth','image','password1','password2')