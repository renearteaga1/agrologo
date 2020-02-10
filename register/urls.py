from django.contrib import admin
from django.urls import path, include


from .views import register

app_name = 'register'

urlpatterns = [
    path('', register, name='register'),
]
