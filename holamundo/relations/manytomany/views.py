from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication


def create(request):

    # articulos
    art1 = Article(headline="articulo 1")
    art1.save()
    art2 = Article(headline="articulo 2")
    art2.save()
    art3 = Article(headline="articulo 3")
    art3.save()

    # publicaciones
    pub1 = Publication(title="publicacion 1")
    pub1.save()
    pub2 = Publication(title="publicacion 2")
    pub2.save()
    pub3 = Publication(title="publicacion 3")
    pub3.save()
    pub4 = Publication(title="publicacion 4")
    pub4.save()
    pub5 = Publication(title="publicacion 5")
    pub5.save()
    pub6 = Publication(title="publicacion 6")
    pub6.save()
    pub7 = Publication(title="publicacion 7")
    pub7.save()

    art1.publications.add(pub1, pub2, pub3)
    art2.publications.add(pub4, pub5)
    art3.publications.add(pub6, pub7)

    # relacionar desde article a publications
    result = art1.publications.all()

    # pub1 = Publication.objects.get(id=1) relacionar desde publications a article
    # result = pub1.article_set.all()

    # eliminar relaciones
    # art1.publications.remove(pub1)

    return HttpResponse(result)
