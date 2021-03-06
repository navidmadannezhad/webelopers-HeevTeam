from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.returnPanelPage, name="returnPanelPage"),
    path('panel/add-product', views.addProduct, name="addProduct"),
    path('panel/become-seller', views.returnBecomeSeller, name="returnBecomeSeller")
]
