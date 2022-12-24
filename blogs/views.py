from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.utils import timezone
from blogs.models import Post, Category #vamos importando nuestros modelos

# Create your views here.

def home_page(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now()
    )
    categories = Category.objects.all()
    featured = Post.objects.filter(featured=True).filter(
        pub_date__lte=timezone.now()
    )[:3]

    context = {
        'post_list': posts,
        'categories': categories,
        'featured': featured
    }

    return render(request, 'blogs/home_page.html', context=context)



class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(
        pub_date__lte=timezone.now()
    )
    #metodo para que tome en cuenta las categorias
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



class PostCreateView(CreateView):
    model = Post
    queryset = Post.objects.filter(
        pub_date__lte=timezone.now()
    )
    fields=['title', 'content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class FeaturedListView(generic.ListView):
    model = Post
    template_name = 'blogs/featured_list.html'

    def get_queryset(self):
        query = Post.objects.filter(featured=True).filter(
            pub_date__lte=timezone.now()
        )
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context