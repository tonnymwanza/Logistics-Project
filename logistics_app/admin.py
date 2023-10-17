from django.contrib import admin
from . models import Product_nature
from . models import Logisticsdetails

# Register your models here.
@admin.register(Product_nature)
class AdminNatureofproducts(admin.ModelAdmin):
    list_display = [
        'nature'
    ]

@admin.register(Logisticsdetails)
class AdminLogisticsdetails(admin.ModelAdmin):
    list_display = [
        'name_of_goods',
        'current_location',
        'destination',
        'nature_of_goods',
        'weight_of_goods',
        'quantity',
        'recipient_name',
        'email_address_of_sender'
    ]