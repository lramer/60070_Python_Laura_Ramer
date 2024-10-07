from django.db import models
from django.contrib.auth.models import User


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
    portada = models.ImageField(upload_to='portadas',blank=True,null=True)   
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} -{self.editorial}"
    

class Coleccion(models.Model):
    descripcion =models.CharField(max_length=200)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    fecha_adquisicion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[('que me faltan', 'que me faltan'), ('disponibles para canje', 'disponibles para canje'), ('en la biblioteca', 'en la biblioteca'), ('Variant Cover', 'Variant Cover')])
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"es la colección {self.descripcion} de {self.usuario}"
    
class Intercambio(models.Model):
    usuario_oferta = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ofertas_enviadas')
    comic_oferta = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='ofertas_enviadas')
    usuario_desea = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ofertas_recibidas')
    comic_deseado = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='ofertas_recibidas')
    fecha_oferta = models.DateTimeField(auto_now_add=True)
    estado_intercambio = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado'), ('rechazado', 'Rechazado')],
        default='pendiente'
    )
    def __str__(self):
        return f'{self.usuario_oferta} - {self.estado_intercambio}'

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    comentario = models.TextField()
    valoracion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 a 5 estrellas
    fecha = models.DateTimeField(auto_now_add=True)   
    def __str__(self):
        return f'{self.comic} Valoracion : {self.valoracion}'

class User_avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    imagen = models.ImageField(upload_to='avatares',blank=True,null=True)        




