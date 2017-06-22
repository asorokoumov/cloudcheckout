from django.db import models

# Create your models here.


class Seller (models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=True, null=True)

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


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comments = models.TextField()

    def __str__(self):
        return self.name


class Delivery(models.Model):
    product = models.ForeignKey(Product)
    delivery_service = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.delivery_service


class Order(models.Model):
    order_nr = models.CharField(max_length=200)
    product = models.ForeignKey(Product)
    product_comments = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    is_delivery_info = models.BooleanField
    delivery_service = models.ForeignKey(Delivery, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    delivery_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.order_nr
