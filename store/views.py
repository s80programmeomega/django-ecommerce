from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpRequest

from .models import Product


def login_user(request: HttpRequest):
    header = {"title": "Login", "text": "Log in to your account!"}
    if request.method == "POST":
        form = request.POST
        username = form.get("username")
        password = form.get("password")
        user = authenticate(
            request=request, username=username, password=password)
        if user:
            login(request=request, user=user)
            messages.success(request, "Login Successful!")
            print("Login Successful!")
            return redirect("store:home")
        else:
            messages.error(
                request, "Fail to login. Invalid username or password!")
            return redirect("store:login")
    return render(request=request, template_name="login_user.html", context={"header": header})


def logout_user(request):
    header = {"title": "Logout", "text": "Welcome to our shop !"}
    logout(request)
    messages.success(request, "Logout successful!")
    return render(request=request, template_name="logout_user.html", context={"header": header})


def home(request):
    products = Product.objects.all().order_by("-id")
    header = {"title": "Shop in style", "text": "Welcome to our shop !"}
    context = {"products": products,
               "header": header}
    return render(request, template_name="home.html", context=context)


def about(request):
    header = {"title": "About Us ...", "text": "lorem"}
    return render(request=request, template_name="about.html", context={"header": header})
