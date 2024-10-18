import os
from django.db import models
from django.db.models.enums import TextChoices
from django.conf import settings


# Categories of products
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250, default="", blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Categories"

    def __repr__(self) -> str:
        return f"Category {self.name}"

    def __str__(self):
        return self.name


# Products
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(max_length=250, default="", blank=True)
    image = models.ImageField(upload_to="uploads/products", blank=True)

    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name="products")

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    #Sale stuff
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Handle requests to image url
    def get_image_url(self):
        # if there is an image with a url
        if self.image and hasattr(self.image, 'url'):
            # if the url contains a file, return its path
            if os.path.isfile(f"{settings.BASE_DIR}{self.image.url}"):
                print(f"isfile ==> {self.image.url}\n")
                return self.image.url
            else:
                print(f"Image file does not exists: {self.image.url}")
                print("Using default image: /media/default/products/default_product.jp")

        return '/media/default/products/default_product.jpg'

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return f"{self.name}, {self.category.name}"

    def __repr__(self) -> str:
        return f"Product({self.name}, {self.price}, Category:{self.category.name})"


# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Customers"

    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}"

    def __repr__(self) -> str:
        return f"Customer({self.first_name}, {self.last_name}, {self.email})"


class OrderStatus(TextChoices):
    PENDING = "pending", "Pending"
    SHIPPED = "shipped", "Shipped"
    DELIVERED = "delivered", "Delivered"
    CANCELLED = "cancelled", "Cancelled"


# Customer Orders
class Order(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE,)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(
        max_length=10, choices=OrderStatus.choices, default=OrderStatus.PENDING,)
    date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Orders"

    def __str__(self) -> str:
        return f"{self.product}"

    def __repr__(self) -> str:
        return f"Order({self.product}, {self.quantity}, {self.customer}, {self.address}, {self.status})"
