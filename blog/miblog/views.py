from django.shortcuts import render
from miblog.models import *
from miblog.forms import *
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# class PostDetalle(DetailView):
#     model = Post
#     template_name = "miblog/posts.html"


def post(request):
    if request.method == "GET":
        posteo = Post.objects.all()
    elif request.method == "POST":
        posteo = Post.objects.all()
    else:
        pass

    categoria = Categoria.objects.all()
    return render(
        request,
        "miblog/posts.html",
        {
            "posteo": posteo,
            "categoria": categoria,
        },
    )


def detail(request, id):
    posteo = Post.objects.filter(id__icontains=id)

    return render(request, "miblog/detalle.html", {"posteo": posteo})


@login_required()
def addPost(request):
    if request.method == "POST":
        formulario1 = FormularioPost(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data

            cadena = info["contenido"]

            # TITULO
            title_end = cadena.find("</h1>")
            title = cadena[4:title_end]

            # DESCRIPCION
            desc_init = cadena.find("<p>")
            desc_end = cadena.find("</p>")
            desc = cadena[desc_init + 3 : desc_end]
            # IMAGEN
            img_init = cadena.find("src")
            if img_init != -1:
                img_init += 5
                img_end = (cadena[img_init:].find('"')) + img_init
                src_imagen = cadena[img_init:img_end]
            else:
                src_imagen = "https://th.bing.com/th/id/R.38317af18aa4e059cedfe29c6e27bedc?rik=i0UrkSLV%2f6PtaA&pid=ImgRaw&r=0"

            postf = Post(
                titulo=title,
                descripcion=desc[:100],
                contenido=info["contenido"],
                categoria_id=request.POST["categoria_id"],
                imagen=src_imagen,
                autor=request.user.username,
            )

            postf.save()
            posteo = Post.objects.all()
            categoria = Categoria.objects.all()
            return render(
                request, "miblog/posts.html", {"posteo": posteo, "categoria": categoria}
            )

    else:
        formulario1 = FormularioPost()

    return render(request, "miblog/addPost.html", {"form1": formulario1})


@login_required
def editarPost(request, id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        formulario1 = FormularioPost(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            cadena = info["contenido"]

            # TITULO
            title_end = cadena.find("</h1>")
            title = cadena[4:title_end]

            # DESCRIPCION
            desc_init = cadena.find("<p>")
            desc_end = cadena.find("</p>")
            desc = cadena[desc_init + 3 : desc_end]
            # IMAGEN
            img_init = cadena.find("src")
            if img_init != -1:
                img_init += 5
                img_end = (cadena[img_init:].find('"')) + img_init
                src_imagen = cadena[img_init:img_end]
            else:
                src_imagen = "https://th.bing.com/th/id/R.38317af18aa4e059cedfe29c6e27bedc?rik=i0UrkSLV%2f6PtaA&pid=ImgRaw&r=0"

            post.contenido = info["contenido"]
            post.imagen = src_imagen
            post.titulo = title
            post.categoria_id = info["categoria_id"]
            post.autor = request.user.username
            post.descripcion = desc[:100]

            post.save()
            posteo = Post.objects.all()
            categoria = Categoria.objects.all()
            return render(
                request, "miblog/posts.html", {"posteo": posteo, "categoria": categoria}
            )
    else:

        formulario1 = FormularioPost(
            initial={"contenido": post.contenido, "categoria": post.categoria}
        )
        print(post.contenido)

    return render(request, "miblog/editarPost.html", {"form1": formulario1})


@login_required()
def borrarPost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    posteo = Post.objects.all()
    categoria = Categoria.objects.all()
    return render(
        request, "miblog/posts.html", {"posteo": posteo, "categoria": categoria}
    )


@login_required()
def addCategoria(request):
    if request.method == "POST":
        nuevaCategoria = FormularioCategoria(request.POST)
        if nuevaCategoria.is_valid():
            info = nuevaCategoria.cleaned_data
            categoriaf = Categoria(titulo=info["titulo"])
            categoriaf.save()

            categoria = Categoria.objects.all()
            posteo = Post.objects.all()
            return render(
                request, "miblog/posts.html", {"posteo": posteo, "categoria": categoria}
            )
    else:
        nuevaCategoria = FormularioCategoria()

    return render(
        request, "miblog/addCategoria.html", {"nuevaCategoria": nuevaCategoria}
    )


def formulario3(request):
    if request.method == "POST":
        formulario3 = FormularioAutor(request.POST)
        if formulario3.is_valid():
            info = formulario3.cleaned_data
            autorf = Autor(nombre=info["nombre"], correo=info["correo"])
            autorf.save()
            return render(request, "miblog/posts.html")
    else:
        formulario3 = FormularioAutor()

    return render(request, "miblog/formu3.html", {"form3": formulario3})


def busqueda(request):
    pass


def buscar(request):
    categoria = Categoria.objects.all()

    if request.GET["titulo"]:
        busqueda = request.GET["titulo"]
        posteo = Post.objects.filter(titulo__icontains=busqueda)
        return render(
            request, "miblog/posts.html", {"posteo": posteo, "categoria": categoria}
        )

    else:
        posteo = Post.objects.all()
        return render(
            request, "miblog/posts.html", {"posteo": posteo, "categoria": categoria}
        )


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            usuario = authenticate(
                username=request.POST["username"],
                password=request.POST["password1"],
            )
            login(request, usuario)
        posteo = Post.objects.all()
        categoria = Categoria.objects.all()
        return render(
            request, "miblog/posts.html", {"posteo": posteo, "categoria": categoria}
        )
    else:
        form = UserCreationForm()

    return render(request, "miblog/registro.html", {"form": form})


def about(request):
    return render(request, "miblog/about.html")
