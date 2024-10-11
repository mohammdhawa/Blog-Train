from django.urls import path
from .views import PostListView, PostDetailView, CreatePost, EditPost, DeletePost


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/new', CreatePost.as_view(), name='create-post'),
    path('posts/edit/<int:pk>', EditPost.as_view(), name='edit-post'),
    path('posts/delete/<int:pk>', DeletePost.as_view(), name='delete-post'),
]
