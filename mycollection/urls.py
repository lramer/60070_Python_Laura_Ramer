from django.urls import path
from .views import inicio_inicio

urlpatterns = [
    
    path('', inicio_inicio, name='inicio'),

]