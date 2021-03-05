from django.shortcuts import render
from django.http import HttpResponse

def userIsAuthenticated(request):
    if request.user.is_authenticated:
        return True
    return False

def returnPanelPage(request):
    if(userIsAuthenticated(request)):
        return render(request,'seller/dashboard.html')
    else:
        return render(request, 'login.html')