from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    
    return render(request, 'posts/post_list.html', {"posts": posts})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    
    return render(request, 'posts/post_detail.html', {'post_detail': post})
