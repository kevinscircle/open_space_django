from django.shortcuts import render

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView
)

from .models import Post
from django.urls import reverse
from .forms import PostForm

# Create your views here.

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post

class CreatePostView(CreateView):
    template_name = 'posts/create.html'
    model = Post
    form_class = PostForm

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('post_list')

class PostDetailsView(DetailView):
    template_name = 'posts/detail.html'
    model = Post


class PostUpdateView(UpdateView):
    template_name = 'posts/update.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_list')