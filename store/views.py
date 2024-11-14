from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Product


def home(request: HttpRequest):
    products = Product.objects.all().order_by("-id")
    header = {"title": "Shop in style", "text": "Welcome to our shop !"}
    context = {"products": products,
               "header": header}
    return render(request, template_name="home.html", context=context)


def about(request: HttpRequest):
    header = {"title": "About Us ...", "text": "lorem"}
    return render(request=request, template_name="about.html", context={"header": header})


def product_details(request: HttpRequest, id: int):
    product = get_object_or_404(Product, id=id)
    print(f'{product=}')
    return render(request=request, template_name="product_details.html", context={"product": product})


def product_category(request: HttpRequest, category: str):
    category = get_object_or_404(Category, name=category)
    print(f"{category=}")
    header = {"title": category.name, "text": category.description}
    products = Product.objects.filter(category=category)
    context = {"products": products, "header": header}
    return render(request, template_name="home.html", context=context)
