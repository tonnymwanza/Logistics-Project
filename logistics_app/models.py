from django.db import models

# Create your models here.
class Product_nature(models.Model):
    nature = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nature

class Logisticsdetails(models.Model):
    name_of_goods    = models.CharField(max_length=255)
    current_location = models.CharField(max_length=50)
    destination      = models.CharField(max_length=70)
    nature_of_goods  = models.ForeignKey(Product_nature, on_delete=models.CASCADE)
    weight_of_goods  = models.IntegerField()
    quantity         = models.IntegerField()
    recipient_name   = models.CharField(max_length=30)
    email_address_of_sender = models.EmailField()

    def __str__(self):
        return self.name_of_goods