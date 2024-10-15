from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
from django.http import HttpRequest
from django.contrib import messages


def register_user(request: HttpRequest):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message="Your registration was successful. You can login now!")
            # Redirect to home after successful registration
            return redirect('user:login')
    else:
        form = RegistrationForm()
    return render(request, 'register_user.html', {'form': form})


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
