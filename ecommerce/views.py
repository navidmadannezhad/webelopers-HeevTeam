from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password

def returnHomePage(request):
    return render(request, 'home.html')

def returnRegisterPage(request):
    return render(request, 'register.html')

def validateUserName(username):
    usernames = User.objects.values('username')
    for un in usernames:
        if un['username'] == username:
            return False
    return True

def validatePasswords(password1, password2):
    if password1 == password2:
        return True 
    return False

def registerUser(request):
    if request.method == 'POST':
        user_is_not_repeated = validateUserName(request.POST['username'])
        passwords_are_equal = validatePasswords(request.POST['password1'],request.POST['password2'])

        errors = []

        if user_is_not_repeated and passwords_are_equal:
            createUser = User.objects.create(first_name= request.POST['first_name'],last_name= request.POST['last_name'], email= request.POST['email'], password= make_password(request.POST['password1']), username= request.POST['username'])
            return render(request, 'login.html')
        else:
            if not user_is_not_repeated:
                errors.append('نام کاربری شما در سیستم موجود است')
            if not passwords_are_equal:
                errors.append('گذرواژه و تکرار گذرواژه یکسان نیستند')

    return render(request, 'register.html', { 'errors': errors })

def returnLoginPage(request):
    return render(request, 'login.html')

def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username= username, password = password)
    if user:
        auth.login(request, user)
        return redirect('/')
    errors = 'نام کاربری یا رمز عبور اشتباه می باشد'
    """ return redirect('/') for davari """ 
    return render(request, 'login.html', { 'errors': errors })

def logoutUser(request):
    auth.logout(request)
    return redirect('/')