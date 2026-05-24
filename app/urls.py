from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base.html"),
    path("inicio", views.index, name="index.html"),
    path("elenco", views.index, name="elenco.html"),
    path("sobre", views.index, name="sobre.html"),
]