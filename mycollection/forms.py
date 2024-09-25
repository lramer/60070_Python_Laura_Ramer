from django import forms
from .models import usuario

class usuarioform(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nombre','user_name','password']

        