from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name = 'nelson', last_name = 'giraldo', email = 'giraldovnelson@gmail.com')
    rep.save()

    art1 = Article(headline = 'prueba de almacenamiento', pub_date = date(day= 11, month= 12, year=2020), reporter = rep)
    art1.save()
    
    art2 = Article(headline = 'prueba de almacenamiento2', pub_date = date(day= 12, month= 12, year=2020), reporter = rep)
    art2.save()
    
    art3 = Article(headline = 'prueba de almacenamiento3', pub_date = date(day= 10, month= 12, year=2020), reporter = rep)
    art3.save()


    #result = art1.reporter.first_name // desde el articulo directamente se puede ingresar a la información del reportero por la llave foranea 

    #result = rep.article_set.filter(headline = 'prueba de almacenamiento2') // desde reportero se debe especificar eñ articulo y se puede traer la información que se requiera

    result = rep.article_set.count() #contar los articulos que tiene relacionado el reportero
    
    

    return HttpResponse (result)


