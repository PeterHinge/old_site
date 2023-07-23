from django.contrib import admin
from .models import Article

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')

admin.site.register(Article, AuthorAdmin)