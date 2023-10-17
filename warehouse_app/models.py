from django.db import models
from logistics_app.models import Product_nature
# Create your models here.

class Warehouse(models.Model):
    name_of_goods = models.CharField(max_length=140)
    nature_of_goods = models.ForeignKey(Product_nature, on_delete=models.CASCADE)
    name_of_owner = models.CharField(max_length=200)
    weight_of_goods = models.IntegerField()
    location = models.CharField(max_length=250)
    email = models.CharField(max_length=222)

    def __str__(self):
        return self.name_of_goods
    
    def get_price(self):
        return self.weight_of_goods * 1000