from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def returnHomePage(request):
    return render(request, 'home.html')

def returnRegisterPage(request):
    return render(request, 'register.html')

def registerUser(request):
    if request.method == 'POST':
        createUser = User.objects.create(first_name= request.POST['first_name'],last_name= request.POST['last_name'], email= request.POST['email'], password= make_password(request.POST['password1']), username= request.POST['username'])


    return render(request, 'register.html')

def returnLoginPage(request):
    return render(request, 'login.html')




""" Working --- """
def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username= username, password = password)
    if user:
        return render(request, 'home.html')
    errors = 'نام کاربری یا رمز عبور اشتباه می باشد'
    return render(request, 'login.html', { 'errors': errors })
