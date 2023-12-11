from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogPostView(ListView):
    model = Post
    template_name = 'home.html'

class DetailPostView(DetailView):
    model = Post
    template_name ='detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields =[ 'title', 'author', 'body']

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView): # deleted
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')