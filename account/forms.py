from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus':'autofocus'}))
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProfileImgForm(forms.ModelForm):
    #Cambiar_imagen = forms.ImageField(widget=forms.FileInput(attrs={"id":"file-img","class":"input-file-hidden"}))
    class Meta:
        model = Profile
        widgets = {
            'image': forms.FileInput(attrs={"id":"file-img","class":"input-file-hidden"})
        }
        fields = ['image']
