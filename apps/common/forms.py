from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]
        
class SignUpForm(forms.ModelForm):
   class Meta:
    model = User
    fields = ['username', 'email', 'password', 'first_name', 'last_name']
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control', }),
        'country': forms.Select(attrs={'class': 'form-control', }),
        'first_name': forms.TextInput(attrs={'class': 'form-control', }),
        'last_name': forms.TextInput(attrs={'class': 'form-control', }),
        'age': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', }),
        'password': forms.PasswordInput(attrs={'class': 'form-control', }),
        'gender': forms.Select(attrs={'class': 'form-control', }),
    }
    labels = {
        'username': ('Username'),
        'country': ('Country'),
        'first_name': ('First Name'),
        'last_name': ('Last Name'),
        'age': ('Birthdate'),
        'email': ('Email'),
        'password': ('Password'),
        'gender': ('Gender'),
    }
    error_messages = {
        'username': {
            'unique': ('The username is not available')
        },
        'first_name': {
            'required': ('The field can not be empty')
        },
        'last_name': {
            'required': ('The field can not be empty')
        },
        'password': {
            'required': ('The field can not be empty')
        }

    }