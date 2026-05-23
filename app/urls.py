from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base.html"),
    path("inicio", views.index, name="index.html"),
]