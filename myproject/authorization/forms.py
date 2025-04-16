from django import forms
from .models import User

class UserForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label= 'Пароль',min_length=3, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')
