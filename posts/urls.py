from django.urls import path
from .views import PostListView, PostDetailView, create_post, edit_post, delete_post


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/new', create_post, name='create-post'),
    path('posts/edit/<int:pk>', edit_post, name='edit-post'),
    path('posts/delete/<int:pk>', delete_post, name='delete-post'),
]
