from django.db import models
from django.utils import timezone

# Create your models here.


class Seller (models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.login


class Product (models.Model):
    seller = models.ForeignKey(Seller)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    development = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Delivery(models.Model):
    product = models.ForeignKey(Product)
    delivery_service = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.delivery_service

