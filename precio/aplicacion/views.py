from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def insumos(request):

    return render(request, "aplicacion/insumos.html")

def personales(request):
    return render(request, "aplicacion/personales.html")

def clientes(request):
    return render(request, "aplicacion/clientes.html")