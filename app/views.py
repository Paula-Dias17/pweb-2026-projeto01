from django.shortcuts import render

def index(request):
    dados_usuario = {"nome": "Michael Douglas", "idade": 23}
    return render(request, "index.html", dados_usuario)

def sobre(request):
    return render(request, "sobre.html")

def elenco(request):
    lista_pokemons = [
        {
            "nome": "Charizard",
            "idade": 0,
            "tipo": "fogo",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Charizard",
            "idade": 0,
            "tipo": "fogo",
            "imagem": "/static/app/imgs/charizard.png"
        }
    ]
        
    context = {"pokedex": lista_pokemons}
    return render(request, "elenco.html", context)
