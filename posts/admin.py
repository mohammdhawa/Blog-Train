from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin



class PostAdmin(SummernoteModelAdmin):
    list_display = ['title', 'id']
    summernote_fields = ['content']
    


admin.site.register(Post, PostAdmin)

admin.site.register(Category)