from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout

 

def register(request:HttpRequest):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
            User.objects.create_user(username=email,email=email, password=password)
            return redirect('login')


    return render(request,"auth/register.html")


def login(request:HttpRequest):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')

    return render(request,"auth/login.html")


def logout_view(request:HttpRequest):
    logout(request)
    return redirect('login')





