from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    is_seller = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


