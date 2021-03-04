from django.shortcuts import render

def returnHomePage(request):
    return render(request, 'home.html')