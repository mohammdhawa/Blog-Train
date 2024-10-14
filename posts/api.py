# Used instead of views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import PostSerializer, CategorySerializer, CommentSerializer
from .models import Post, Category, Comment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class PaginationOfPosts(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'


@api_view(['GET'])
def post_list_api(request):
    posts = Post.objects.all()
    data = PostSerializer(posts, many=True).data
    
    return Response({'data': data})

class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PaginationOfPosts
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'draft', 'author']
    search_fields = ['title']
    

class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPI(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class CommentListAPI(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PaginationOfPosts
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
