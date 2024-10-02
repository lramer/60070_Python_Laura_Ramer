from django.urls import path
from .views import *

urlpatterns = [
    
    path('', inicio_inicio, name='inicio'),
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