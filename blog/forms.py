from django import forms
#  importamos los modelos a conectar
from blog.models import Post, Comment

# formulario para los Post


class PostForm(forms.ModelForm):

    class Meta():
        # conectamos al modelo
        model = Post
        # los campos del formulario asumen el tipo de datos del modelo
        fields = ('author', 'title', 'text')
        # asignamos clases CSS a los elementos del formulario
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }


# formulario para los comentarios
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
