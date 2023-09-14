
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name= 'saludo'),
    path('despedida/', views.despedida, name= 'despedida'),
    path('adulto/<int:edad>/', views.adulto, name = 'adulto')
]
