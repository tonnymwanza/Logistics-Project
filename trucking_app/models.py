from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Trucking(models.Model):
    license_number = models.IntegerField()
    vehicle_brand = models.CharField(max_length=200)
    cargo_of_choice = models.TextField()
    age = models.IntegerField()
    location = models.CharField(max_length=150)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.vehicle_brand