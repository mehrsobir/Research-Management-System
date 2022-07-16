from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Post
from users.models import NewUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Ҳатмист! Лутфан, емайли дурустро ворид созед!!")
    class Meta:
        model = NewUser
        fields = ["first_name", "last_name", "email", "password1", "password2"]


