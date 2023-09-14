from django.shortcuts import render
from .models import Autor, Entry
from django.http import HttpResponse

# modificar registros y actualizar valores
def update(request):
    author = Autor.objects.get(id=1)
    author.name = "nelson"
    author.email = "giraldovnelson@gmail.com"
    author.save()
    return HttpResponse("modificado el registro")

def queries(request):
    #obtener todos los elementos
    autores = Autor.objects.all()

    #obtener los datos filtrando por condiciones
    filtrado = Autor.objects.filter(email = 'barbernicholas@example.org')

    #obtener un unico objeto filtrado
    authorUnico = Autor.objects.get(id=1)
    
    #obtener una cantidad de registros definida
    limite = Autor.objects.all()[:10]

    # Obtener los registros saltando los 5 primeros
    offsets = Autor.objects.all()[5:10] 

    #order by
    order = Autor.objects.all().order_by('email')

    #obtener los elementos cuyo id sea menor o igual a 15
    menorIgual = Autor.objects.filter(id__lte = 15)

    #obtener los elementos cuyo id sea mayor o igual a 15
    mayorIgual = Autor.objects.filter(id__gte = 15)

    #obtener los elementos cuyo id sea menor a 15
    menor = Autor.objects.filter(id__lt = 15)

    #obtener los elementos cuyo id sea mayor a 15
    mayor = Autor.objects.filter(id__gt = 15)

    #obtener los elementos cuyo id contenga un 5
    contener = Autor.objects.filter(id__contains = 5)

    #obtener los elementos cuyo id sea 5
    exacto = Autor.objects.filter(id__exact = 5)

    return render(request, 'post/queries.html', {'autores':autores, 'filtrado': filtrado, 'authorUnico': authorUnico, 
        'limite': limite, 'offsets':offsets,'order':order, 'menorIgual':menorIgual, 'mayorIgual': mayorIgual, 'menor': menor, 
        'mayor': mayor, 'contener': contener, 'exacto': exacto})  #se hace render de la pagina y se le indican los contextos a mostrar




