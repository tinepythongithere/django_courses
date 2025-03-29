from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def home(request):

    return render(request, 'carboneapp/home.html')

def login_view(request):

    if 'login_submit' in request.POST:
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('carboneapp:home')
        else:
            messages.error(request, 'User introuvable')
    return render(request, 'carboneapp/login.html')

def logout_view(request):
    logout(request)

    return redirect('carboneapp:login')
