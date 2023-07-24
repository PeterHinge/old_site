from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user_name', 'user_email',  'published_date', 'status')
    list_filter = ('status', 'published_date')
    search_fields = ('user_name', 'user_email', 'content')