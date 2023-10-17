from django.contrib import admin
from . models import Warehouse
# Register your models here.

@admin.register(Warehouse)
class AdminWarehouse(admin.ModelAdmin):
    list_display = [
        "name_of_goods",
        "nature_of_goods",
        "name_of_owner",
        "weight_of_goods",
        "location",
        "email"
    ]