from django.shortcuts import render

# Create your views here.
def cadastro(request):
    return render(request, 'cadastro.html')


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    return render(request, 'logout.html')