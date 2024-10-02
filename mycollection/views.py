from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .models import Comic ,Coleccion #usuario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
#from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def inicio_inicio(req):

    plantila = loader.get_template('index.html')
    documento = plantila.render({})
    return HttpResponse(documento)

### ini ver que eliminar

### fin ver que eliminar

class comicList(ListView):

    model = Comic
    template_name = 'lista_comics.html'
    context_object_name = 'comics'

class comicDetalle(DetailView):

    model = Comic
    template_name = 'detail_comics.html'
    context_object_name = 'comics'    

class comicCreate(CreateView):
    model = Comic
    template_name = 'create_comics.html'    
    fields = ('__all__')
    success_url = '/inicio'

class comicUpdate(UpdateView):
    model = Comic
    template_name = 'update_comics.html'    
    fields = ('__all__')
    success_url = '/inicio'    
    context_object_name = 'comics'

class comicDelete(DeleteView):    
    model = Comic
    template_name = 'delete_comics.html'      
    success_url = '/inicio'


class coleccionlist(ListView):
    model = Coleccion
    template_name = 'lista_coleccion.html'   
    context_object_name = 'coleccion'

class coleccionDetalle(DetailView):
    model = Coleccion
    template_name = 'detalle_coleccion.html'   
    context_object_name = 'coleccion'

class coleccionCreate(CreateView):
    model = Coleccion
    template_name = 'create_coleccion.html'    
    fields = ('__all__')
    success_url = '/inicio'

class coleccionUpdate(UpdateView):
    model = Coleccion
    template_name = 'update_coleccion.html'    
    fields = ('__all__')
    success_url = '/inicio'    
    context_object_name = 'coleccion'

class coleccionDelete(DeleteView):    
    model = Coleccion
    template_name = 'delete_coleccion.html'      
    success_url = '/inicio'    



