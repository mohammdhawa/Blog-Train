from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=50000)
    draft = models.BooleanField()
    publish_date = models.DateTimeField(default=timezone.now())
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts/')
    author = models.ForeignKey('Author', related_name='author_post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='category_post', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title[:50]


class Author(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
