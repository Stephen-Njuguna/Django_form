from django.urls import path
from .views import BlogPostView,DetailPostView,BlogCreateView,BlogUpdateView,BlogDeleteView


urlpatterns = [
path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post_delete'),
path('post/<int:pk>/edit/',
BlogUpdateView.as_view(), name='post_edit'), # new
path('post/new/', BlogCreateView.as_view(), name='post_new'),
path('post/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
path('', BlogPostView.as_view(), name='home'),
]