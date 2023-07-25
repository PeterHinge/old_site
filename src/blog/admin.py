from django.contrib import admin
from .models import Article, Comment, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'key_words')


@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'author', 'slug')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', 'status')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user_name', 'user_email',  'published_date', 'status')
    list_filter = ('status', 'published_date')
    search_fields = ('user_name', 'user_email', 'content')