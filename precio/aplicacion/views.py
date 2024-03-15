from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def insumos(request):
    contexto = {'insumos':Insumo.objects.all()}
    return render(request, "aplicacion/insumos.html",contexto)

def personales(request):
    return render(request, "aplicacion/personales.html")

def clientes(request):
    return render(request, "aplicacion/clientes.html")