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
    form = ContactForm()

    return render(request, 'widget.html', {'form': form})
