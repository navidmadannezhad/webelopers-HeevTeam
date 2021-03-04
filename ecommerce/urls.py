from django.urls import path
from . import views

urlpatterns = [
    path('', views.returnHomePage, name="homePage"),
    path('register/', views.returnRegisterPage, name="registerPage"),
    path('register-user/', views.registerUser, name="registerUser")
]
