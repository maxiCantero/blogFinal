from django import forms

class FormularioPost(forms.Form):
    titulo = forms.CharField()
    contenido = forms.CharField()
    # categoria = forms.ForeignKey(Categoria, on_delete=forms.CASCADE)
    # autor = forms.ForeignKey(Autor, on_delete=forms.CASCADE)

class FormularioCategoria(forms.Form):
    titulo = forms.CharField()

class FormularioAutor(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()



