from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}

    summernote_fields = ('ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    
# Register your models here.
