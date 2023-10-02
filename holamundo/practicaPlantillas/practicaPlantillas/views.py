from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    return render(request, 'index.html', {})


def porfatolio(request):
    return render(request, 'portafolio.html', {})


def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})
