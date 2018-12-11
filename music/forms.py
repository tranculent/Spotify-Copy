# generic user class
from django.contrib.auth.models import User
from django import forms

# new user class


class UserForm(forms.ModelForm):
    # textfield where the chars are hidden
    password = forms.CharField(widget=forms.PasswordInput)

    # information about class
    class Meta:
        model = User
        # what to appear on the form
        fields = ['username', 'email', 'password']