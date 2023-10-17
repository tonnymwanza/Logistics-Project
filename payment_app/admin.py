from django.contrib import admin
from . models import Billing, Cart, Specifications
# Register your models here.

@admin.register(Billing)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "firstname",
        "secondname",
        "email_address",
        "location",
        "payment_mode",
        "country",
        "zip",
        "company_name",
        "phone_number",
        "address_line"
    ]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        "delivered",
        "pending"
    ]

@admin.register(Specifications)
class SpecificationsAdmin(admin.ModelAdmin):
    list_display = [
        "name_of_goods",
        "nature_of_goods",
        "name_of_owner",
        "weight_of_goods",
        "location",
        "email"
    ]