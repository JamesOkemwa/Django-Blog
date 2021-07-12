from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: 
        #specifies the model we want this form to interact with
        model = User
        fields = ['username', 'email', 'password1', 'password2']
