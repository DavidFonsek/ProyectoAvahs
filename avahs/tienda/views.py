from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")

def novedades(request):
    return render(request, "pages/novedades.html")