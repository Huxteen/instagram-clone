from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ( 
            'username',
            'password1',
            'password2',
        )