from django.shortcuts import render
from miblog.models import *
from miblog.forms import *
from django.http import HttpResponse

def post(request):
    posteo = Post.objects.all()
    categoria = Categoria.objects.all()
    return render(request,"miblog/posts.html",{"posteo":posteo,"categoria":categoria})

def formulario1(request):
    if request.method=='POST':
        formulario1 = FormularioPost(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            postf = Post(titulo=info["titulo"], contenido=info['contenido'])
            postf.save()
            return render(request,"miblog/index.html")
    else:
        formulario1 = FormularioPost()
    return render(request,"miblog/formu1.html",{"form1":formulario1})

def formulario2(request):
    if request.method=='POST':
        formulario2 = FormularioCategoria(request.POST)
        if formulario2.is_valid():
            info = formulario2.cleaned_data
            categoriaf = Categoria(titulo=info["titulo"])
            categoriaf.save()
            return render(request,"miblog/index.html")
    else:
        formulario2 = FormularioCategoria()
    return render(request,"miblog/formu2.html",{"form2":formulario2})

def formulario3(request):
    if request.method=='POST':
        formulario3 = FormularioAutor(request.POST)
        if formulario3.is_valid():
            info = formulario3.cleaned_data
            autorf = Autor(nombre=info['nombre'], correo=info['correo'])
            autorf.save()
            return render(request,"miblog/index1.html")
    else:
        formulario3 = FormularioAutor()
    return render(request,"miblog/formu3.html",{"form3":formulario3})

def busquedaCategoria(request):
    return render(request,"miblog/busquedaCategoria.html")

def buscar(request):
    if request.GET["titulo"]:
        busqueda = request.GET["titulo"]
        categorias = Categoria.objects.filter(titulo__icontains=busqueda)
        return render(request,"miblog/resultados.html",{"categorias":categorias})
    else:
        return render(request,"miblog/index1.html")
