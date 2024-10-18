from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="product/<int:id>", view=views.product_details, name="product_details"),
    path(route="about/", view=views.about, name="about"),
]
