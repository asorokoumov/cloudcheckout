from django.db import models
from django.utils import timezone

# Create your models here.


class Seller (models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name