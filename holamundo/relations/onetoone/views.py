from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant


def create(request):
    #crear elementos 
    place = Place(name = "Lugar1", address = "calle 1")
    place.save()

    restaurant = Restaurant(place = place, number_of_employees = 8)
    restaurant.save()
    return HttpResponse(restaurant.place.name)
