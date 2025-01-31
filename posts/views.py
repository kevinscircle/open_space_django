from django.shortcuts import render

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)

from .models import Post, Comment
from django.urls import reverse
# from .forms import PostForm, UpdatePostForm
from .forms import PostForm

from django.http import HttpResponseRedirect

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
    
class PostUpdateView2(UpdateView):
    template_name = 'posts/update2.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_list')


class PostDeleteView(DeleteView):
      # no template, jast delete and send to list 
    model = Post

    def get_success_url(self):
        return reverse('post_list')
    
    def get(self, requests, *args, **kwargs):
        # in order to skip confirmation page
        return self.post(requests, *args, **kwargs)  
    
    def post(self, requests, *args, **kwargs):
        # delete the post
        self.object = self.get_object()
        self.object.delete()
        # return super().post(requests, *args, **kwargs)
        return HttpResponseRedirect(self.get_success_url())
        
        
    # ** if one wants confirmation when deleting 
    	# create template
    	#   template_name = 'posts/delete_post.html'
    	
    	# delete code below get_success_url
    	
    	# template
    	# 	wrap in <form>
    	# 	add delete button
    	# 	add
    	# 		{% crsf_token %}


class CommentListView(ListView):
    template_name = 'comments/list_comment.html'
    model = Comment