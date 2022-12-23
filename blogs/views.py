from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from blogs.models import Post, Category #vamos importando nuestros modelos

# Create your views here.

def home_page(request):
    #Con esto obtenemos todos los post y categorias
    posts=Post.objects.all()
    categories=Category.objects.all()
    featured=Post.objects.filter(featured=True) [:3]

    context={
        'post_list':posts,
        'categories':categories,
        'featured':featured
    }

    return render(request, 'blogs/home_page.html', context=context)



class PostDetailView(generic.DetailView):
    model=Post
