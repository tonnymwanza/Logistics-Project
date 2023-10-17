from django.shortcuts import render
from . form import BillingForm
from django.contrib import messages
from warehouse_app.models import Warehouse
from . models import Billing
# Create your views here.
obj = Warehouse.objects.all()
def checkout(request):
    form = BillingForm()
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            billing = Billing.objects.create(
            firstname = form.cleaned_data["firstname"],
            secondname = form.cleaned_data["secondname"],
            email_address = form.cleaned_data["email_address"],
            location = form.cleaned_data["location"],
            payment_mode = form.cleaned_data["payment_mode"],
            country = form.cleaned_data["country"],
            zip = form.cleaned_data["zip"],
            company_name = form.cleaned_data["company_name"],
            address_line = form.cleaned_data["address_line"],
            phone_number = form.cleaned_data["phone_number"],
            )
            messages.success(request, "Payment successful. Go to cart to truck the shipment")
        else:
            form = BillingForm()    
    context = {
        "form": form
    }
    return render(request, "checkout.html", context)
