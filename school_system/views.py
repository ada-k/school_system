from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# def index(request):
#     context = {

#     }
#     return render(request, 'index.html', context)

def login_view(request):
    username= request.POST.get('username')
    password= request.POST.get('password')
    user= authenticate(request, username = username, password=password)
    if user is not None:
        login(request, user)
        if request.user.is_authenticated:
            return render(request, "school.html")
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)

    return redirect("login")
