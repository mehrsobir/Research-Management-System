from .models import Account, Profile
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Рамзи мавҷуда",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "autofocus": True,
                   "placeholder": "рамзи мавҷуда" }
        ),
    )
    new_password1 = forms.CharField(
        label="Рамзи нав",
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "рамзи нав"}
        ),
    )
    new_password2 = forms.CharField(
        label="Такрори рамзи нав",
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "такрори рамзи нав"}
        ),
    )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'nationality', 'education', 'gender', 'image']
