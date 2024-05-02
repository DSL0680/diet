from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='필수 입력 항목입니다.')
    last_name = forms.CharField(max_length=30, required=True, help_text='필수 입력 항목입니다.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
