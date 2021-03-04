from django.urls import path
from . import views

urlpatterns = [
    path('', views.returnHomePage, name="homePage")
]
