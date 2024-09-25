from django import forms
from .models import usuario, Coleccion,Comic

class usuarioform(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nombre','user_name','password']

class Comicform(forms.ModelForm):
    class Meta:
        model = Comic
        fields =['titulo','autor','editorial','fecha_publicacion','numero_edicion','descripcion','valor','stock']
        