from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")

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

def login(request):
    return render(request, "pages/login.html")

def registro(request):
    return render(request, "pages/registro.html")

def carrito(request):
    return render(request, "pages/carrito.html")

