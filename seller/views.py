from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product

def userIsAuthenticated(request):
    if request.user.is_authenticated:
        return True
    return False

def returnPanelPage(request):
    if(userIsAuthenticated(request)):
        return render(request,'seller/dashboard.html')
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