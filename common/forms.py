from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    

    class Meta:
        model = User
        fields = ("name","username", "email","phone_number","communication_purpose", 
        "understanding_purpose","teacher","parent","other_purpose" )