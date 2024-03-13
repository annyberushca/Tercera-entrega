from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('insumos/',insumos,name="insumos"),
    path('personales/',personales,name="personales"),
    path('clientes/',clientes,name="clientes"),
]

