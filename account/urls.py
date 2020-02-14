from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include


from .views import register, account, profile_img

app_name = 'account'

urlpatterns = [
    path('', account, name='account'),
    path('profile-img-changed/', profile_img, name='profile_img'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
