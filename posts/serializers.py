# Instead of form (it converts data to JSON)
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'
