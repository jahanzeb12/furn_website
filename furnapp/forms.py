from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username','email','password1','password2']
class CustomLoginForm(AuthenticationForm):
	username = UsernameField(
		label='',
		widget=forms.TextInput(attrs={'class':'form-control,h1','placeholder':'Username'})
	)
	password=forms.CharField(
		label="",
		strip=False ,
		widget=forms.PasswordInput(attrs={'class':'form-control,h1','placeholder':'Password'}),
	)

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
    	super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class':'form-control,h1',
        'placeholder': 'Email Address',
        'type': 'email',
        'name': 'email'
        }))


class orderform(ModelForm):
	class Meta:
		model= cart
		fields =['product_id','quantity','customer_id']

class commentform(ModelForm):
	class Meta:
		model=review
		fields=['name','email','comment']
		widgets={
            'name':forms.TextInput(attrs={'class':'form-control h1','placeholder':'Name','style':'height:40px;font-size:18px;color:black;border:1px solid coral;'}),
			'email':forms.TextInput(attrs={'class':'form-control h1','placeholder':'Email','style':'height:40px;font-size:18px;color:black;border:1px solid coral;'}),
			'comment':forms.Textarea(attrs={'class':'form-control h1','placeholder':'Review','style':'height:40px;font-size:18px;color:black;border:1px solid coral;'})
		}

class contactform(ModelForm):
	class Meta:
		model=contact
		fields=['name','email','message']
		widgets={
            'name':forms.TextInput(attrs={'class':'form-control h1','placeholder':'Name','style':'height:40px;font-size:18px;color:black;border:1px solid coral;'}),
			'email':forms.TextInput(attrs={'class':'form-control h1','placeholder':'Email','style':'height:40px;font-size:18px;color:black;border:1px solid coral;'}),
			'message':forms.Textarea(attrs={'class':'form-control h1','placeholder':'Message','style':'height:40px;font-size:18px;color:black;border:1px solid coral;'})
        }

