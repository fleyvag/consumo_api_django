import requests
  
def getnamepokemon(id):
    url=f'https://pokeapi.co/api/v2/pokemon/{id}'
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
    nombre=data.get('name',[])
    getsprite=data.get('sprites',[])
    getimg=getsprite.get('other',[])
    getimgother=getimg.get('dream_world',[])
    imagen=getimgother.get('front_default',[])
    # datos={
    #     'nombre': nombre,
    #     'imagen' : imagen,
    # }
    datos=(nombre,imagen)
    return datos
    # return print(datos)

def regresar_lista_pokes():
    i=0
    listaname=[]
    listaimg=[] 
    for i in range(0,15):
        i=i+1
        lista=getnamepokemon(i)
        listaname.append(lista[0])
        listaimg.append(lista[1])
    data={
        
        'sprite':listaimg  
    }
   
    return data

