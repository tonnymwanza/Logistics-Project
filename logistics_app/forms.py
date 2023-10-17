from django import forms
from . models import Logisticsdetails

class LogisticsdetailsForm(forms.ModelForm):
    class Meta:
        model = Logisticsdetails
        fields = [
            "name_of_goods",
            "current_location",
            "destination",
            "nature_of_goods",
            "weight_of_goods",
            "quantity",
            "recipient_name",
            "email_address_of_sender"
        ]