from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="about/", view=views.about, name="about"),
    path(route="login/", view=views.login_user, name="login"),
    path(route="logout/", view=views.logout_user, name="logout"),
]
