from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib import messages

from .forms import RegisterForm

# Create your views here.
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
    return render(request, 'register/register.html', context)

# class LoginView(LoginView):
#     if not User.is_authenticated():
#         render ()
