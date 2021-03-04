from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def returnHomePage(request):
    return render(request, 'home.html')

def returnRegisterPage(request):
    return render(request, 'register.html')

def registerUser(request):
    if request.method == 'POST':
        createUser = User.objects.create(first_name= request.POST['first_name'],last_name= request.POST['last_name'], email= request.POST['email'], password= request.POST['password1'], username= request.POST['username'])


    return render(request, 'register.html')
