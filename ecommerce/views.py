from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password
from Webelopers.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from seller.models import Seller
from seller.models import Product


def userIsAuthenticated(request):
    if request.user.is_authenticated:
        return True
    return False


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
            user = User.objects.create(first_name= request.POST['first_name'],last_name= request.POST['last_name'], email= request.POST['email'], password= make_password(request.POST['password1']), username= request.POST['username'])
            user.save()
            seller = Seller.objects.create(user = user)
            seller.save()
            return render(request, 'login.html')
        else:
            if not user_is_not_repeated:
                errors.append('نام کاربری شما در سیستم موجود است')
            if not passwords_are_equal:
                errors.append('گذرواژه و تکرار گذرواژه یکسان نیستند')

    return render(request, 'register.html', { 'errors': errors })



def Login(request):
    if request.method == 'GET':
        if userIsAuthenticated(request):
            return redirect('/seller/panel')
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password = password)
        if user:
            auth.login(request, user)
            return redirect('/seller/panel')
        return redirect('/')


def logoutUser(request):
    auth.logout(request)
    return redirect('/')


def contactUs(request):
    if request.method == 'GET':
        return render(request, 'contact-us.html')
    elif request.method == 'POST':
        subject = request.POST['title']
        message = request.POST['text']
        sender = request.POST['email']
        letters = 'ا ب پ ت ث ج چ ح خ د ذ ر ز ژ ص ض ط ظ ع غ ف ق ک گ ل م ن و ه'
        letters = letters.replace(' ','')
        for letter in letters:
            if letter in message or letter in subject:
                return redirect('/')
        if len(message) < 10 or len(message) > 250:
            return redirect('/contact-us')
        else:
            if request.method == 'POST':
                reciever = 'navidproject283@gmail.com '
                send_mail(subject, 
                    message, sender,[reciever], fail_silently = False)
                return render(request, 'contact-us.html', {'contact_success_message': 'success'})
            return redirect('/contact-us')



def returnProductPage(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'products.html',data)

def searchFor(request):
    query = request.POST['searchValue']
    products = []
    productsByName = Product.objects.filter(name__contains = query)
    productsByDesc = Product.objects.filter(description__contains = query)
    if productsByName:
        products = productsByName
    if productsByDesc:
        products = productsByDesc | productsByName
    data = {
        'products': products
    }
    return render(request, 'products.html',data)
            






