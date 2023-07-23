from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post (models.Model):

    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
        
    all_articles = models.Manager()
    published_manager = PublishedManager() 
    
    options = (
    ('draft', 'Draft'),
    ('ready', 'Ready'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey (User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        ordering = ('-published_date',)

    def get_absolute_url(self):
        return reverse('blog:post_single',args=[self.slug])

    def __str__(self):
        return self.title