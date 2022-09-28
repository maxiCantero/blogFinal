from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.EmailField()

class Categoria(models.Model):
    titulo = models.CharField(max_length=30)

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=140)
    fecha_creacion = models.DateField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,null=True)