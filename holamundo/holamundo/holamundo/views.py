from django.http import HttpResponse


def saludo(request):
   return HttpResponse("Hola mundo") 

def despedida(request):
   return HttpResponse("chao mundo") 

def adulto(request, edad):
   if edad >= 18:
      return HttpResponse("eres mayor de edad")
   else:
      return HttpResponse("no eres mayor de edad")