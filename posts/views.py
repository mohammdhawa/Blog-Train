from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView)
# from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
    
    
class CreatePost(CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = '__all__'
    success_url = '/'


class EditPost(UpdateView):
    model = Post
    template_name = 'posts/new.html'
    fields = '__all__'
    success_url = '/'


class DeletePost(DeleteView):
    model = Post
    success_url = '/'
