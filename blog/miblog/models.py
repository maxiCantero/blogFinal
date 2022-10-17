from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo


class Post(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    contenido = RichTextField()
    fecha_creacion = models.DateField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    autor = models.CharField(max_length=30, null=True)
    imagen = models.CharField(max_length=200, null=True)
