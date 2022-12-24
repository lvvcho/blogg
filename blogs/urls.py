from django.urls import path
from blogs import views
from .views import PostCreateView

app_name='blogs'

urlpatterns = [
    path('', views.home_page),
    path('post/new', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
    path('featured/', views.FeaturedListView.as_view(), name='featured'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]

