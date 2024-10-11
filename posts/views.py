from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView)
from .forms import CommentForm


class PostListView(ListView):
    model = Post


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.post = post
            myform.save()
            return redirect(f"/post-detail/{pk}")
    
    return render(request, 'posts/post_detail.html', {'object': post, 'comments': comments, 'form': form})
    
    
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
