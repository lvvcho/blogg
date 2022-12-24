from django.urls import path
from blogs import views
from .views import PostCreateView, CategoryListView, PostDetailView, FeaturedListView, SearchResultsView

app_name='blogs'

urlpatterns = [
    path('', views.home_page),
    path('post/new', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
    path('featured/', views.FeaturedListView.as_view(), name='featured'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<int:pk>', views.CategoryListView.as_view(), name='category'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
]

