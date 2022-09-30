from django.shortcuts import render
from miblog.models import *
from miblog.forms import *
from django.http import HttpResponse

def post(request):
    if request.method=='GET':
        posteo = Post.objects.all()
        # search = request.GET['titulo']
        # posteo = Post.objects.filter(titulo__startswith=search)
    else:
        pass
        

    categoria = Categoria.objects.all()
    return render(request,"miblog/posts.html",{"posteo":posteo,"categoria":categoria})

def formulario1(request):
    if request.method=='POST':
        formulario1 = FormularioPost(request.POST)
        if formulario1.is_valid():
            # print(request.GET['categoria_id'])
            info = formulario1.cleaned_data
            
            postf = Post(titulo=info["titulo"], descripcion = info['descripcion'],contenido=info['contenido'], categoria_id=request.POST['categoria_id'])
            # print(info['categoria_id'])
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

def busqueda(request):
    pass

def buscar(request):
    categoria = Categoria.objects.all()
    if request.GET["titulo"]:
        busqueda = request.GET["titulo"]
        posteo = Post.objects.filter(titulo__icontains=busqueda)
        return render(request,"miblog/posts.html",{"posteo":posteo,"categoria":categoria})
    else:
        posteo = Post.objects.all()
        print("paso por todo")
        return render(request,"miblog/posts.html",{"posteo":posteo,"categoria":categoria})
