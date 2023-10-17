from django.contrib import admin
from . models import Trucking
# Register your models here.

@admin.register(Trucking)
class AdminTrucking(admin.ModelAdmin):
    list_display = [
        "license_number",
        "vehicle_brand",
        "cargo_of_choice",
        "age",
        "location",
        "email"
    ]
