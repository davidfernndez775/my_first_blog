from django import forms
#  importamos los modelos a conectar
from blog.models import Post, Comment


# formulario para los Post


## Las clase meta son definiciones de parametros y no requere (), los () son para llamadas a funciones o heredar de otra clase

class PostForm(forms.ModelForm):
    class Meta:
        # conectamos al modelo
        model = Post
        # los campos del formulario asumen el tipo de datos del modelo
        fields = ('author', 'title', 'text')
        # asignamos clases CSS a los elementos del formulario
        widgets = {
            'author': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.fields.get("author", None) and user:
            self.fields['author'].initial = user


# formulario para los comentarios
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
