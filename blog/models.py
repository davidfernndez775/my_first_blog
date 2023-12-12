from django.db import models
# importamos el controlador de fecha y hora
from django.utils import timezone
# importamos reverse para ir a una url despues de una operacion
from django.urls import reverse


# Create your models here.

# creamos la clase para los post del blog


class Post(models.Model):
    # creamos el autor vinculado a un superuser para que tenga permisos para publicar
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # los campos DateTimeField poseen dos parametros importantes a conocer
    # auto_now  =>  este campo especifica que en cada .save que reciba el objeto la fecha se guardara
    # auto_now_add  =>  este campo especifica que se guardara la fecha solo al momento de crearse el objeto, sustituyes por el default que tenias
    create_date = models.DateTimeField(auto_now_add=True)
    # la fecha de publicacion puede quedar en blanco porque no este publicado todavia
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        '''define la fecha de publicacion de un post'''
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        '''chequea si un comentario esta aprobado'''
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        '''funcion por defecto para cuando termine de crear un post vaya a una url determinada'''
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title


# creamos la clase comentario


class Comment(models.Model):
    # conectamos el comentario con el post al que comenta
    post = models.ForeignKey(
        'blog.Post', related_name='comments', on_delete=models.CASCADE)
    # el autor de un comentario no tiene que ser un superuser
    author = models.CharField(max_length=200)
    text = models.TextField()
    # lo mismo especificado en el campo de arriba
    create_date = models.DateTimeField(auto_now_add=True)
    # los comentarios necesitan ser aprobados antes de mostrarse, al principio estan en False
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        '''aprueba una comentario'''
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        '''en este caso como hay que esperar que sea aprobado se va a la url de la lista de post'''
        return reverse("post_list", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.text
