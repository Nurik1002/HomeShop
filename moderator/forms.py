from django import forms
from django.contrib.auth.forms import UserCreationForm
from moderator.models import MainUser



class UserRegisterForm(UserCreationForm):
    '''User registration form'''
    
    email = forms.EmailField()
    phone_num = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    
    class  Meta:
        model = MainUser
        fields = ['username', 'email', 'phone_num', 'password1', 'password2']
        
        
    
    
