from datetime import date
from django.http import HttpRequest
from .models import Category

def get_all_categories(request: HttpRequest):
    return {"categories": Category.objects.all()}

def get_current_year(request: HttpRequest):
    print(f" ==> {date.today()} <==")
    return {"this_year": date.today().year}