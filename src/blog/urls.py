from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('article/<slug:article>/', views.single_article, name='article'),
    path('category/<category>/', views.CategoryListView.as_view(), name='category'),
]