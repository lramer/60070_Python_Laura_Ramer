from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import usuario,Coleccion,Comic

# Create your views here.
def inicio_inicio(req):

    plantila = loader.get_template('index.html')
    documento = plantila.render({})
    return HttpResponse(documento)