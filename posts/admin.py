from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(SummernoteModelAdmin):
    list_display = ['title', 'id']
    list_filter = ['category', 'tags', 'draft']
    summernote_fields = ['content']
    
    inlines = [CommentInline]
        
    
    


admin.site.register(Post, PostAdmin)

admin.site.register(Category)

# admin.site.register(Comment)