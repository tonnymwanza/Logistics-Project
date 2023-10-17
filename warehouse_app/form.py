from django import forms
from . models import Warehouse

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = [
            "name_of_goods",
            "nature_of_goods",
            "name_of_owner",
            "weight_of_goods",
            "location",
            "email"
        ]