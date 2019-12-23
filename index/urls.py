from django.contrib import admin
from django.urls import path, include

from .views import indexView

app_name = 'index'

urlpatterns = [
    path('', indexView, name='index'),
]
