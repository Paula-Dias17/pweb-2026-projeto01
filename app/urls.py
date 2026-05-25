from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index.html"),
    path("inicio", views.index, name="index.html"),
    path("elenco", views.elenco, name="elenco.html"),
    path("sobre", views.sobre, name="sobre.html"),
]