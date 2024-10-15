from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpRequest

from .models import Product


def home(request):
    products = Product.objects.all().order_by("-id")
    header = {"title": "Shop in style", "text": "Welcome to our shop !"}
    context = {"products": products,
               "header": header}
    return render(request, template_name="home.html", context=context)


def about(request):
    header = {"title": "About Us ...", "text": "lorem"}
    return render(request=request, template_name="about.html", context={"header": header})
