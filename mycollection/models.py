from django.db import models

class usuario(models.Model):
    nombre = models.CharField(max_length=200) # type: ignore
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name


# Create your models here.
class Comic(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editorial = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    numero_edicion = models.IntegerField()
    descripcion = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.titulo} - {self.numero_edicion}ª Edición"
    

class Coleccion(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='coleccion')
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    fecha_adquisicion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[('nuevo', 'Nuevo'), ('usado', 'Usado')])

    def __str__(self):
        return f"{self.comic.titulo} en la colección de {self.usuario.user_name}"
    




