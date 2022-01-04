from django.shortcuts import render
from .services import *

# Create your views here.
def consumoapi(request):
    context_object_name = "obj"
    # context = {
    #     'pokemons':regresar_lista_pokes(),
    #     'img':regresar_lista_img()
    # }
    context = regresar_lista_pokes()
    

    return render(request, 'index.html', context)


