
from django.urls import path
from . import views


urlpatterns = [
    path("home", views.home),
    path("novedades", views.novedades),
    path("descuentos", views.descuentos),
    path("tendencias", views.tendencias),
    path("novedades/elemento", views.elemento),
    path("resultados", views.resultados),
]

