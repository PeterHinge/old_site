from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):

    published_posts = Post.published_manager.all()

    return render(request, 'home.html', {'posts' : published_posts})

def single_article(request, post):

    post = get_object_or_404(Post, slug=post, status='published')

    return render(request, 'article.html', {'post' : post})