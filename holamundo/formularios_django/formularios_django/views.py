from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm


def form(request):
    comment_form = CommentForm(
        {'name': 'nelson', 'url': 'http://elmas-capi.to', 'comment': 'Elma canon moreno'})
    return render(request, 'form.html', {'comment_form': comment_form})


def goal(request):
    if request.method != 'POST':
        return HttpResponse("metodo no permitido")

    return HttpResponse("datos guardados a nombre de: " + request.POST['name'])


def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # aqui van todas las acciones necesarias cuando todos los datos son correctos
            return HttpResponse("valido")
        else:
            # aquí se hacen las acciones a tomar cuando los datos no son validos, como avisar a usuario que no es correcto y que lo modifique
            return render(request, 'widget.html', {'form': form})
