from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def novedades(request):
    return render(request, "novedades.html")