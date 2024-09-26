from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .models import usuario,Coleccion,Comic
from .forms import usuarioform,Comicform

# Create your views here.
def inicio_inicio(req):

    plantila = loader.get_template('index.html')
    documento = plantila.render({})
    return HttpResponse(documento)

def guardar_usuario(req):
    if req.method == 'POST':
        form = usuarioform(req.POST)
        if form.is_valid():
            form.save()  
            plantila = loader.get_template('index.html')
            documento = plantila.render({})
            return HttpResponse(documento)
    else:
        form = usuarioform()
    
    context = {'form': form}
    return render(req, 'nuevo_usuario.html', context)

def nuevo_titulo(req):
    if req.method == 'POST':
        form = Comicform(req.POST)
        if form.is_valid():
            form.save()  
            plantila = loader.get_template('index.html')
            documento = plantila.render({})
            return HttpResponse(documento)
    else:
        form = Comicform()
    
    context = {'form': form}
    return render(req, 'nuevo_titulo.html', context)

def mostrar_comics(req):
    comics = Comic.objects.all()
    context = {'comics':comics }
    return render(req,'listar_comics.html',context)


def busqueda_comics(req):
    return render(req,'buscar_comics.html')


def buscar(req): 
    if req.GET['titulo']:
        nuevo_titulo = req.GET['titulo']
        comics = Comic.objects.filter(titulo__icontains=nuevo_titulo)
        return render(req,'buscar_comics.html',{'titulo':comics.titulo,'autor':comics.autor,'editorial':comics.editorial,'fecha_publicacion':comics.fecha_publicacion,'numero_edicion':comics.numero_edicion,'descripcion':comics.descripcion,'valor':comics.valor,'stock':comics.stock})

    else:
        respuesta = 'No se encontraron resultados '

        return HttpResponse(respuesta)


