from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import UserProfile

from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length= 100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required= True, label= 'Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',  'email', 'password1', 'password2']
        

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length= 100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required= True, label= 'Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'birth_date','company_name','occupation' ,'profile_picture']