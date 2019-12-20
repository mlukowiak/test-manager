from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Nick'}))
    email = forms.EmailField(label="", help_text="", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    password1 = forms.CharField(label="", help_text="", widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(label="", help_text="", widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']