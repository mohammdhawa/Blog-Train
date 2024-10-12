# Used instead of views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post


@api_view(['GET'])
def post_list_api(request):
    posts = Post.objects.all()
    data = PostSerializer(posts, many=True).data
    
    return Response({'data': data})

class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostUpdateAPI(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer