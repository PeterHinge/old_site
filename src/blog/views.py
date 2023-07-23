from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):

    published_articles = Article.published_articles.all()

    return render(request, 'home.html', {'articles' : published_articles})

def single_article(request, article):

    article = get_object_or_404(Article, slug=article, status='published')

    return render(request, 'article.html', {'article' : article})