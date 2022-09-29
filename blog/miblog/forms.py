from django import forms
from .models import Categoria

class FormularioPost(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'style':'width:20em'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'style':'width:20em'}))
    contenido = forms.CharField(widget=forms.Textarea(attrs={'style':'width:20em'}))
    categoria_id = forms.ModelChoiceField(queryset = Categoria.objects.all(),widget=forms.Select(attrs={'style':'width:20em'}))
    # autor = forms.ForeignKey(Autor, on_delete=forms.CASCADE)

class FormularioCategoria(forms.Form):
    titulo = forms.CharField()

class FormularioAutor(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()



