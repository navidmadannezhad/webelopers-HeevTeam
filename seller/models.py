from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    is_seller = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name= "user")

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, related_name= "seller")
    description = models.TextField(null = True, max_length = 200)

    def __str__(self):
        return self.name


