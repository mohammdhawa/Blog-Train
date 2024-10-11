from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=50000)
    draft = models.BooleanField()
    publish_date = models.DateTimeField(default=timezone.now())
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(User, related_name='author_post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='category_post', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title[:50]


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000)
    create_at = models.DateTimeField(default=timezone.now())
    