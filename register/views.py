from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterForm

# Create your views here.
def register(request):
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
    context = {
        'form' : form,
    }
    return render(request, 'register/register.html', context)
