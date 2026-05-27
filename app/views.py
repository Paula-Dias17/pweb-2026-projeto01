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
            "nome": "Gardevoir",
            "idade": 0,
            "tipo": "psiquico/fada",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Jigglypuff",
            "idade": 0,
            "tipo": "normal/fada",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Liepard",
            "idade": 0,
            "tipo": "sombrio",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Mew",
            "idade": 0,
            "tipo": "psiquico",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Mimikyu",
            "idade": 0,
            "tipo": "fantasma/fada",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "psyduck",
            "idade": 0,
            "tipo": "agua",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Piplup",
            "idade": 0,
            "tipo": "agua",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Snorlax",
            "idade": 0,
            "tipo": "normal",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Sylveon",
            "idade": 0,
            "tipo": "fada",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Togepi",
            "idade": 0,
            "tipo": "normal",
            "imagem": "/static/app/imgs/charizard.png"
        }
    ]
        
    context = {"pokedex": lista_pokemons}
    return render(request, "elenco.html", context)
