from django.shortcuts import render

from .models import Producto


def home(request):
    return render(request, "pages/home.html")

def novedades(request):
    return render(request, "pages/secciones/novedades.html")

def descuentos(request):
    productos = Producto.objects.all()
    cant_items = len(productos)
    data = {
        'lista_productos': productos,
        'items': cant_items
    } 
    return render(request, "pages/secciones/descuentos.html", data)

def tendencias(request):
    return render(request, "pages/secciones/tendencias.html")

def elemento(request):
    return render(request, "pages/elemento.html")

def resultados(request):
    return render(request, "pages/resultados.html")

def login(request):
    return render(request, "pages/login.html")

def registro(request):
    return render(request, "pages/registro.html")

def carrito(request):
    return render(request, "pages/carrito.html")

