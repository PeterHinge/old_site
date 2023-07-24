from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):

    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
        
    all_articles = models.Manager()
    published_articles = PublishedManager() 
    
    options = (
    ('draft', 'Draft'),
    ('ready', 'Ready'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published_date')
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey (User, on_delete=models.CASCADE, related_name='blog_posts')
    # excerpt = models.TextField(null=True)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        ordering = ('-published_date',)

    def get_absolute_url(self):
        return reverse('blog:single_article', args=[self.slug])

    def __str__(self):
        return self.title

class Comment(models.Model):

    article = models.ForeignKey(Article,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('published_date',)

    def __str__(self):
        return f'Comment by {self.user_name}'
