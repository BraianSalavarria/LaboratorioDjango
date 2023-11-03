from django.shortcuts import render


def home(request):
    return render(request, 'base/base.html')

def login(request):
    return render(request, 'login/login.html')