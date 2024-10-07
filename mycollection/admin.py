from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import *



admin.site.register(Comic)
admin.site.register(Coleccion)
admin.site.register(Comentario)
admin.site.register(Intercambio)
admin.site.register(User_avatar)

