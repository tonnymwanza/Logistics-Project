from django import forms
from . models import payment_choices
from . models import Billing

class BillingForm(forms.Form):
    firstname =forms.CharField(max_length=200)
    secondname =forms.CharField(max_length=200)
    email_address = forms.EmailField()
    location = forms.CharField(max_length=255)
    payment_mode  = forms.ChoiceField(widget=forms.RadioSelect, choices=payment_choices)
    country = forms.CharField(max_length=255)
    zip = forms.IntegerField()
    company_name = forms.CharField(max_length=255)
    phone_number = forms.IntegerField()
    address_line = forms.CharField(max_length=255)