from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterForm, ProfileForm
from .models import Profile

# Create your views here.
def account(request, *args, **kwargs):
    if request.user.is_authenticated:
        print('sii autenthicades')
        if request.method == 'POST':
            form_profile = ProfileForm()
            form_user = UserChangeForm()
            if form.is_valid():
                form.save()
            return redirect('index:index')
        else:
            user = get_object_or_404(Profile, user=request.user)
            form_profile = ProfileForm(instance=user)
            form_user = UserChangeForm(instance=request.user)
        context = {
            'form_profile' : form_profile,
            'form_user' : form_user,
        }
    else:
        print('noooo autenthicades')
        return redirect ('account:login')
    return render(request, 'account/account.html', context)

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                email = form.cleaned_data.get('email')
                obj.username = email
                messages.success(request, f'Usuario creado: {email}')
                obj.save()
                login(request, obj)
            return redirect('index:index')
        else:
            form = RegisterForm()
    else:
        return redirect('index:index')
    context = {
        'form' : form,
    }
    return render(request, 'account/register.html', context)
