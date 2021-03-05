from django.contrib import admin
from .models import Seller
from .models import Product

admin.site.register(Seller)
admin.site.register(Product)