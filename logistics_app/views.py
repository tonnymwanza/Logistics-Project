from django.shortcuts import render, redirect
from .forms import LogisticsdetailsForm
from django.contrib import messages
from . models import Logisticsdetails
global price
# Create your views here.
def index(request):
    return render(request, "index.html")

def logistics(request):
    form = LogisticsdetailsForm()
    if request.method == "POST":
        form = LogisticsdetailsForm(request.POST or None)
        if form.is_valid():
            name_of_goods = form.cleaned_data["name_of_goods"]
            current_location = form.cleaned_data["current_location"]
            destination = form.cleaned_data["destination"]
            nature_of_goods = form.cleaned_data["nature_of_goods"]
            weight_of_goods = form.cleaned_data["weight_of_goods"]
            quantity = form.cleaned_data["quantity"]
            recipient_name = form.cleaned_data["recipient_name"]
            form.save()
            global price #declaration of price as a global variable
            price = weight_of_goods * 1000
            #print(price)
        else:
            form = LogisticsdetailsForm()
    context = {
        "form":form,
        "price":price
    }
    return render(request, "logistics.html", context)

def about(request):
    return render(request, "about.html")
