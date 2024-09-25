from django.urls import path
from .views import inicio_inicio,guardar_usuario,nuevo_titulo

urlpatterns = [
    
    path('', inicio_inicio, name='inicio'),
    path('Usuario/', guardar_usuario, name='usuario'),
    path('', guardar_usuario, name='usuario'),
    path('comics/', nuevo_titulo, name='comics'),
    path('', nuevo_titulo, name='comics'),

]