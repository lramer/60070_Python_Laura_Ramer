from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from .forms import *

urlpatterns = [
    
    path('', inicio_inicio, name='inicio'),
    path('login/',login_request, name='login'),
    path('logout/',LogoutView.as_view(template_name= 'logout.html'), name='logout'),

    path('nuevo_usuario/', registro , name='nuevo_usuario'),
    path('editar_perfil/', edit_user , name='editar_perfil'),
    path('crear_avatar/', agregar_avatar , name='crear_avatar'),
    
    path('lista_comics/', comicList.as_view(), name='lista_comics'),
    path('detalle_comics/', comicDetalle.as_view(), name='detalle_comics'),
    path('crear_comics/', comicCreate.as_view(), name='crear_comics'),
    path('modifica_comics/', comicUpdate.as_view(), name='modifica_comics'),
    path('elimina_comics/', comicDelete.as_view(), name='elimina_comics'),


    path('colecciones/', coleccionlist.as_view(), name='colecciones'),
    path('detalle_coleccion/', coleccionDetalle.as_view(), name='detalle_coleccion'),
    path('crear_coleccion/', coleccionCreate.as_view(), name='crear_coleccion'),
    path('modifica_coleccion/', coleccionUpdate.as_view(), name='modifica_coleccion'),
    path('elimina_coleccion/', coleccionDelete.as_view(), name='elimina_coleccion'),

]