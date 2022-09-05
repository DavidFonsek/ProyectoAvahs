from django.shortcuts import render
from .models import Producto


def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    } 
    
    return render(request, "pages/home.html",data)

def novedades(request):
    return render(request, "pages/novedades.html")

def descuentos(request):
    return render(request, "pages/descuentos.html")

def tendencias(request):
    return render(request, "pages/tendencias.html")

def elemento(request):
    return render(request, "pages/elemento.html")

def resultados(request):
    return render(request, "pages/resultados.html")

def carrito(request):
    return render(request, "pages/carrito.html")

def login(request):
    return render(request, "registration/login.html")
 
def registro(request):
    return render(request, "registration/registro.html")

def agregar(request):
    return render(request,"pages/agregar.html")

