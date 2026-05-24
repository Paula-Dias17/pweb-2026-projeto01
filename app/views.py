from django.shortcuts import render

def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def elenco(request):
    return render(request, "elenco.html")



# Create your views here.
