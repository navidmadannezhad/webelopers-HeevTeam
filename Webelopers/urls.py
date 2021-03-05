from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce.urls')),
    path('seller/', include('seller.urls')),
    path('', include('django.contrib.auth.urls')),
]
