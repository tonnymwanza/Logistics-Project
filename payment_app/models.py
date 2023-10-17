from django.db import models
from warehouse_app.models import Warehouse
# Create your models here.
payment_choices = (
    ("M", "M-pesa"),
    ("P", "Paypal"),
    ("O", "On-delivery")
)
country_of_choice = (
    ("K", "Kenya"),
    ("T", "Tanzania"),
    ("U", "Uganda"),
    ("B", "Burundi"),
    ("R", "Rwanda"),
    ("S", "Sudan")
)

class Billing(models.Model):
    firstname = models.CharField(max_length=255)
    secondname = models.CharField(max_length=255)
    email_address = models.EmailField()
    location = models.CharField(max_length=255)
    payment_mode = models.CharField(max_length=1, choices=payment_choices, default="M-pesa")
    country = models.CharField(max_length=1, choices=country_of_choice, default="Kenya")
    zip = models.IntegerField(default=100)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField()
    address_line = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.firstname
    
class Cart(models.Model):
    delivered = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)
    
    def __str__(self):
        return self.delivered
    
class Specifications(Warehouse):
    pass

