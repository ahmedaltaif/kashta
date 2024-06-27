from django.shortcuts import render
from articles.models import Topic, Article

def home(request):
    topics = Topic.objects.all().prefetch_related('articles')
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'website/home.html', {'topics': topics, 'articles': articles})