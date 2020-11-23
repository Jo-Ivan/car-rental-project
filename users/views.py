from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        # login user
        return
    else:
        return render(request, 'users/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'users/dashboard.html')
