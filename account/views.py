from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterForm

# Create your views here.
def account(request, *args, **kwargs):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserChangeForm(request.user.id, request.POST)
            if form.is_valid():
                form.save()
            return redirect('index:index')
        else:
            form = UserChangeForm()
    context = {
        'form' : form,
    }
    return render(request, 'account/account.html', context)

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.username = form.cleaned_data.get('email')
                email = form.cleaned_data.get('email')
                messages.success(request, f'Usuario creado: {email}')
                obj.save()

            return redirect('index:index')
        else:
            form = RegisterForm()
    else:
        return redirect('index:index')
    context = {
        'form' : form,
    }
    return render(request, 'account/register.html', context)
