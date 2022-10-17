from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class FormularioPost(forms.Form):

    # descripcion = forms.CharField(widget=forms.TextInput(attrs={"style": "width:20em"}))
    # contenido = forms.CharField(widget=forms.Textarea(attrs={'style':'width:20em'}))
    contenido = forms.CharField(widget=CKEditorWidget())
    categoria_id = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={"style": "width:20em"}),
    )
    # autor = forms.ForeignKey(Autor, on_delete=forms.CASCADE)
    class Meta:
        model = Post


class FormularioSearch(forms.Form):
    pass


class FormularioCategoria(forms.Form):
    titulo = forms.CharField()


class FormularioAutor(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()
