from django.shortcuts import render

def index(request):
    return render(request, 'index.html',{})

def porfatolio(request):
    return render(request, 'portafolio.html', {})

def login(request):
    return render(request, 'login.html', {})
