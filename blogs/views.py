from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.utils import timezone
from django.db.models import Q
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
    fields=['title', 'content', 'categories']

    def get_queryset(self):
        query = Post.objects.filter(featured=True).filter(
            pub_date__lte=timezone.now()
        )
        return query

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class FeaturedListView(generic.ListView):
    model = Post
    template_name = 'blogs/results.html'

    def get_queryset(self):
        query = Post.objects.filter(featured=True).filter(
            pub_date__lte=timezone.now()
        )
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryListView(generic.ListView):
    model = Post
    template_name = 'blogs/results.html'

    def get_queryset(self):
        query = self.request.path.replace('/category/', '')
        print(query)
        post_list = Post.objects.filter(categories__id=query).filter(
            pub_date__lte=timezone.now()
        )
        return post_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'blogs/results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')  #conseguimos el input que el usuario ingreso en el search   
        post_list = Post.objects.filter(
            Q(title__icontains=query)|Q(categories__title__icontains=query) #filtramos post cuyo titulo contenga el query que paso el usuario
        ).filter(
            pub_date__lte=timezone.now()
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
