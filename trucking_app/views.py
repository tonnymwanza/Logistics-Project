from django.shortcuts import render, redirect
from . form import TruckingForm
from django.contrib import messages
# Create your views here.

def trucking(request):
    fom = TruckingForm()
    if request.method == "POST":
        fom = TruckingForm(request.POST or None)
        if fom.is_valid():
            license_number = fom.cleaned_data["license_number"]
            vehicle_brand = fom.cleaned_data["vehicle_brand"]
            cargo_of_choice = fom.cleaned_data["cargo_of_choice"]
            location = fom.cleaned_data["location"]
            age = fom.cleaned_data["age"]
            email = fom.cleaned_data["email"]
            fom.save()
            messages.success(request, "Application submitted successfully. We will get back to you soon.")
        else:
            messages.error(request, "data not send")
    context = {
        "fom":fom
    }
    return render(request, "trucking.html", context)