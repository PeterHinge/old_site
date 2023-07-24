from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Article
from .forms import NewCommentForm

def home(request):

    published_articles = Article.published_articles.all()

    return render(request, 'home.html', {'articles' : published_articles})

def single_article(request, article):

    article = get_object_or_404(Article, slug=article, status='published')

    comments = article.comments.filter(status=True)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.article = article
            user_comment.save()
            return HttpResponseRedirect('/blog/' + article.slug)
    else:
        comment_form = NewCommentForm()
    return render(request, 'article.html', {'article' : article, 'comment':  user_comment, 'comments': comments, 'comment_form': comment_form})
