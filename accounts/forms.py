from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    password = forms.CharField()
    confirm_password = forms.CharField()


    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "password"]