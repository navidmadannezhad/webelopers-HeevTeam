from django.urls import path
from . import views

urlpatterns = [
    path('', views.returnHomePage, name="homePage"),
    path('register/', views.returnRegisterPage, name="registerPage"),
    path('register-user/', views.registerUser, name="registerUser"),
    path('login/', views.returnLoginPage, name="loginPage"),
    path('login-user/', views.loginUser, name="loginUser"),
    path('logout-user/', views.logoutUser, name="logoutUser"),
]
