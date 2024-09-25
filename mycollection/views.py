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

def guardar_usuario(request):
    if request.method == 'POST':
        form = usuarioform(request.POST)
        if form.is_valid():
            form.save()  
            plantila = loader.get_template('index.html')
            documento = plantila.render({})
            return HttpResponse(documento)
    else:
        form = usuarioform()
    
    context = {'form': form}
    return render(request, 'nuevo_usuario.html', context)

def nuevo_titulo(request):
    if request.method == 'POST':
        form = Comicform(request.POST)
        if form.is_valid():
            form.save()  
            plantila = loader.get_template('index.html')
            documento = plantila.render({})
            return HttpResponse(documento)
    else:
        form = Comicform()
    
    context = {'form': form}
    return render(request, 'nuevo_titulo.html', context)