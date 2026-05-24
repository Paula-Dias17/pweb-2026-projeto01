from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base.html"),
    path("inicio", views.index, name="index.html"),
    path("elenco", views.elenco, name="elenco.html"),
    path("sobre", views.sobre, name="sobre.html"),
]