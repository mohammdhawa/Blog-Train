from django.urls import path
from .views import PostListView, post_detail, CreatePost, EditPost, DeletePost
from .api import PostListAPI, PostDetailAPI, CategoryListAPI, CommentListAPI, CategoryDetailAPI


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post-detail/<int:pk>', post_detail, name='post-detail'),
    path('posts/new', CreatePost.as_view(), name='create-post'),
    path('posts/edit/<int:pk>', EditPost.as_view(), name='edit-post'),
    path('posts/delete/<int:pk>', DeletePost.as_view(), name='delete-post'),
    
    # API
    path('api/categories/', CategoryListAPI.as_view(), name='categories'),
    path('api/categories/<int:pk>/', CategoryDetailAPI.as_view(), name='categories'),
    path('api/comments', CommentListAPI.as_view(), name='comments'),
    path('api/posts', PostListAPI.as_view(), name='posts-api'),
    path('api/post-detail/<int:pk>', PostDetailAPI.as_view(), name='post-detail'),
    
    
    # path('api/post-edit/<int:pk>', PostUpdateAPI.as_view(), name='post-edit')
]
