from django.db import models


from cmath import log
from bs4 import BeautifulSoup
import requests
import time

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=100000, decimal_places=5)
   
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name