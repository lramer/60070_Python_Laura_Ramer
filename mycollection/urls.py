from django.urls import path
from .views import inicio_inicio,guardar_usuario

urlpatterns = [
    
    path('', inicio_inicio, name='inicio'),
    path('/Usuario/', guardar_usuario, name='usuario'),
    path('', guardar_usuario, name='usuario'),

]