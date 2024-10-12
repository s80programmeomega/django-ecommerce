from django.contrib import admin
from .models import Category, Product, Customer, Order
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",  "description",
                    "date_added", "last_modified")
    list_display_links = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "description",
                    "category", "image", "date_added", "last_modified")
    list_display_links = ("id", "name")

    def image(self, obj: Product):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="50"/>')
        return '(No Image)'
    image.short_description = 'Thumbnail'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email" ,"phone", "date_added", "last_modified"]
    
    list_display_links = ["id", "email", "first_name",]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "product", "quantity", "address", "phone", "status", "date", "last_modified")
    
    list_display_links = ("id", "product", "customer",)
