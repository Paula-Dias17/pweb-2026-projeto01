from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def elenco(request):
    lista_pokemons = [
        {
            "nome": "Charizard",
            "num": 0,
            "tipo": "fogo",
            "sobre": "",
            "imagem": "/static/app/imgs/charizard.png"
        },
        {
            "nome": "Gardevoir",
            "num": 0,
            "tipo": "Psiquico/Fada",
            "imagem": "/static/app/imgs/gardevoir.png"
        },
        {
            "nome": "Jigglypuff",
            "num": 0,
            "tipo": "Normal/Fada",
            "imagem": "/static/app/imgs/jigglypuff.png"
        },
        {
            "nome": "Liepard",
            "num": 0,
            "tipo": "Sombrioo",
            "imagem": "/static/app/imgs/lierpard.png"
        },
        {
            "nome": "Mew",
            "num": 0,
            "tipo": "Psiquico",
            "imagem": "/static/app/imgs/mew.png"
        },
        {
            "nome": "Mimikyu",
            "num": 0,
            "tipo": "Fantasma/Fada",
            "imagem": "/static/app/imgs/mimikyu.png"
        },
        {
            "nome": "psyduck",
            "num": 0,
            "tipo": "Água",
            "imagem": "/static/app/imgs/psyduck.png"
        },
        {
            "nome": "Piplup",
            "num": 0,
            "tipo": "Água",
            "imagem": "/static/app/imgs/piplup.png"
        },
        {
            "nome": "Snorlax",
            "num": 0,
            "tipo": "Normal",
            "imagem": "/static/app/imgs/snorlax.png"
        },
        {
            "nome": "Sylveon",
            "num": 0,
            "tipo": "Fada",
            "imagem": "/static/app/imgs/sylveon.png"
        },
        {
            "nome": "Togepi",
            "num": 0,
            "tipo": "Normal",
            "imagem": "/static/app/imgs/togepi.png"
        }
    ]
        
    context = {"pokedex": lista_pokemons}
    return render(request, "elenco.html", context)
