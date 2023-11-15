from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url="login_page/")
def home(request):
    return render(request, 'home.html', {"messages": messages})

# Login View
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login has run")
            messages.success(request, "You have logged in successfully!")
            return redirect("home")
        else:
            messages.error(request, "Your credentials were incorrect")
            return redirect("login_page")
        
    return render(request, 'login.html', {"messages": messages})


def logout_page(request):
    logout(request)
    messages.success(request, "You are logged out.")
    return redirect("login_page")