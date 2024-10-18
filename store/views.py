from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import Product


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
