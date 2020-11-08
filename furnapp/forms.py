from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username','email','password1','password2']
class CustomLoginForm(AuthenticationForm):
	username = UsernameField(
		label='',
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
	)
	password=forms.CharField(
		label="",
		strip=False ,
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
	)