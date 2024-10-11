from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
    
    
def create_post(request):
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/')
    
    return render(request, 'posts/new.html', {'form': form})


def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    
    form = PostForm(instance=post)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect(f"/post-detail/{pk}")

    return render(request, 'posts/new.html', {'form': form})


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    
    post.delete()
    
    return redirect('/')
