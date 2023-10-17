from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.

def registration(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname  = request.POST["lastname"]
        email     = request.POST["email"]
        username  = request.POST["username"]
        password  = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.success(request, "the username is taken")
                return redirect("registration.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "the email is already in use")
                return redirect("registration.html")
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,password=password, username=username)
                user.save();
                return redirect("registration_success")
        else:
            messages.info(request, "the passwords do not match")
            return redirect("registration")
    return render(request, "registration.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "incorrect username or password")
            return redirect("login")
    return render(request, "login.html")

def registration_success(request):
    return render(request, "registration_success.html")