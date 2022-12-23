from django.db import models
from django.conf import settings
from users.models import User
from django.urls import reverse

# Create your models here.

#Clase post la cual tiene su titulo, slug, overview, fecha de creado, contenido y autor.
class Post(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)  
    overview=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    categories=models.ManyToManyField('Category')   #un post puede tener varias categorias y una categoria puede tener muchos post=ManyToManyField
    featured=models.BooleanField(default=False)

    #funcion la cual entrega el slug de cada post
    def get_absolute_url(self):
        return reverse("blogs:post", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title



class Category(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("blogs:category", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title