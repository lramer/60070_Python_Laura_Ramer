from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required   
from .forms import *
from .models import *

# Create your views here.
def inicio_inicio(req):
    try:
        avatar = User_avatar.objects.get(User=req.user.id)
        return render(req,'index.html',{'imge': avatar.image.url})
    except:
        return render(req,'index.html',{})

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


class comicUpdate(LoginRequiredMixin,UpdateView):
    model = Comic
    template_name = 'update_comics.html'    
    fields = ('__all__')
    success_url = '/inicio'    
    context_object_name = 'comics'


class comicDelete(LoginRequiredMixin,DeleteView):    
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


class coleccionCreate(LoginRequiredMixin,CreateView):
    model = Coleccion
    template_name = 'create_coleccion.html'    
    fields = ('__all__')
    success_url = '/inicio'


class coleccionUpdate(LoginRequiredMixin,UpdateView):
    model = Coleccion
    template_name = 'update_coleccion.html'    
    fields = ('__all__')
    success_url = '/inicio'    
    context_object_name = 'coleccion'


class coleccionDelete(LoginRequiredMixin,DeleteView):    
    model = Coleccion
    template_name = 'delete_coleccion.html'      
    success_url = '/inicio'   



def login_request(req):
    if req.method == 'POST':

        form = AuthenticationForm(req, data = req.POST)
    
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            pswd = form.cleaned_data.get('password')

            user = authenticate(username = usuario,password = pswd)

            if user:
                login(req,user)

                return render(req,'index.html',{"mensaje":f" Bienvenido al sitio! {usuario}"})  
            else:
                return render(req,'index.html',{"mensaje":" Datos Incorrectos "})  
        else:
            return render(req,'login.html',{'form':form})  

    form = AuthenticationForm()
    return render(req,'login.html',{'form':form})


def registro(req):

    if req.method == 'POST':

        form = UserCreationForm(req.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            form.save()           

            return render(req,'index.html',{'mensaje':f'Usuario : {usuario} Creado exitosamente.'})  
        else:
            return render(req,'create_user.html',{'form': form}) 

    else:
        form = UserCreationForm(req.POST)
        return render(req,'create_user.html',{'form': form})      
    
@login_required
def edit_user(req):

    usuario = req.user

    if req.method == 'POST':

        form = UserEditForm(req.POST,instance = req.user )
        if form.is_valid():
            data = form.cleaned_data
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data['password2'])
            usuario.save()           

            return render(req,'index.html',{'mensaje':f'Datos Actualizados exitosamente.'})  
        else:
            return render(req,'update_user.html',{'form': form}) 

    else:
        form = UserEditForm(instance = req.user)
        return render(req,'update_user.html',{'form': form})  


@login_required()
def agregar_avatar(req):

  if req.method == 'POST':
    
    form= createavatarform(req.POST, req.FILES)
    if form.is_valid():

      data = form.cleaned_data
      avatar = User_avatar(user=req.user, imagen=data['imagen'])
      avatar.save()

      return render(req, 'index.html', { 'mensaje': f'Avatar creado correctamente!'})

    else:
      return render(req, 'create_avatar.html', { 'form': form })    

  else:

    form =createavatarform()
    return render(req, 'create_avatar.html', { 'form': form })    







