from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .models import Seller
from django.contrib.auth.models import User, Group

def userIsAuthenticated(request):
    if request.user.is_authenticated:
        return True
    return False

def userIsSeller(request):
    seller = getActiveSeller(request)
    if seller.is_seller:
        return True
    return False


def returnBecomeSeller(request):
    if request.method == 'GET':
        if userIsAuthenticated(request):
            return render(request, 'seller/become-seller.html')
        else:
            return redirect('/login/')
    elif request.method == 'POST':
        seller = getActiveSeller(seller)
        seller.is_seller = True
        seller.save()
    return render(request, 'seller/dashboard.html')

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
        description = request.POST['description']
        seller = getActiveSeller(request)
        product = Product.objects.create(name=name, quantity=quantity, price=price, seller = seller, description = description)
        product.save()

    return redirect('/seller/panel/add-product')


def getActiveSeller(request):
    user = User.objects.get(username = request.user.username)
    seller = Seller.objects.get(user_id = user.id)
    return seller

def myProducts(request):
    if userIsAuthenticated(request) and userIsSeller(request):
        seller = getActiveSeller(request)
        products = Product.objects.filter(seller_id = seller.id)
        return render(request, 'seller/my-products.html', {'products': products})


def editProduct():
    pass