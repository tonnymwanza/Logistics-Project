from django import forms 
from . models import Trucking

class TruckingForm(forms.ModelForm):
    class Meta:
        model = Trucking
        fields = [
            "license_number",
            "vehicle_brand",
            "cargo_of_choice",
            "location",
            "age",
            "email"
        ]