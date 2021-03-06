from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .models import Seller
from django.contrib.auth.models import User, Group

def userIsAuthenticated(request):
    if request.user.is_authenticated:
        return True
    return False

def createGroupOf(groupname):
    groupDoesNotExist = not Group.objects.get(name = groupname)
    if groupDoesNotExist:
        Group.objects.create(name = groupname)

def userIsSeller(request):
    if request.user.groups.filter(name = 'seller').exists():
        return True
    return False


def returnBecomeSeller(request):
    if request.method == 'GET':
        return render(request, 'seller/become-seller.html')
    elif request.method == 'POST':
        createGroupOf('seller')
        request.user.groups.add('seller')
        return redirect('/seller/panel/')

def returnPanelPage(request):
    if userIsAuthenticated(request) and userIsSeller(request):
        return render(request, 'seller/dashboard.html')
    elif userIsAuthenticated(request):
        return render(request,'seller/become-seller.html')
    else:
        return render(request, 'login.html')


def addProduct(request):
    if request.method == 'GET':
        return render(request, 'seller/add-product.html')
    elif request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        Product.objects.create(name=name, quantity=quantity, price=price)

    return redirect('/seller/panel/add-product')