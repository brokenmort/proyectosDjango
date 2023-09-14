from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test (request):
    return HttpResponse("funciona melo")

def create (request):
    #comment = Comment(name = "Nelson", score=5, comment = "este es un comentario") ---> objeto construido para contener el registro a grabar
    #comment.save()      ------> De este forma se crea manual un registro en la tabla especificando los valores a llenar
    #comment = Comment.objects.create(name = "jhonatan")  ---> de esta forma se crea manual un registro de una manera mas generica, dejando los valores predeterminados
    return HttpResponse("Ruta para probar la creación de modelos")

def delete(request):
    #comment = Comment.objects.get(id = 2) ---> objeto construido para contener el registro a borrar
    #comment.delete() ----> de esta forma se borra un registro especificando el id
    #Comment.objects.filter(id="4").delete() -----> de esta forma de borra un registro identificando el id
    return HttpResponse ("Ruta para probar los borrados")