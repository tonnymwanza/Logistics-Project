from django.shortcuts import render, redirect
from . form import WarehouseForm
from django.contrib import messages
from . models import Warehouse
# Create your views here.
def warehouse(request):
    fom = WarehouseForm()
    if request.method == "POST":
        fom = WarehouseForm(request.POST)
        if fom.is_valid():
            name_of_goods = fom.cleaned_data["name_of_goods"]
            nature_of_goods = fom.cleaned_data["nature_of_goods"]
            name_of_owner = fom.cleaned_data["name_of_owner"]
            weight_of_goods = fom.cleaned_data["weight_of_goods"]
            location = fom.cleaned_data["location"]
            email = fom.cleaned_data["email"]
            fom.save()
            price = weight_of_goods * 1000
            return redirect("checkout")
        else:
            messages.error(request, "error sending data")
    context = {
        "fom":fom,
        "price":price
    }
    return render(request, "warehouse.html", context)