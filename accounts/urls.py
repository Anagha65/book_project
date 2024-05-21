from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('register',views.Register_user,name='register'),
    path('login',views.loginUser, name='login'),
    path('logout/',views.logOut, name='logout'),
    path('home/',views.HomePage,name='home')

]


