from django.shortcuts import render

def index(request):
    context = {

    }
    return render(request, 'index.html', context)

def login_view(request):
    username= request.POST.get('username')
    password= request.POST.get('password')
    user= authenticate(request, username = username, password=password)
    if user is not None:
        login(request, user)
        if request.user.is_authenticated:
            return render(request, "index.html")
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message":"Logged Out."})