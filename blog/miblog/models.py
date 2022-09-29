from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.EmailField()

class Categoria(models.Model):
    titulo = models.CharField(max_length=30)
    def __str__(self):
        return self.titulo
class Post(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    contenido = models.CharField(max_length=600)
    fecha_creacion = models.DateField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,null=True)