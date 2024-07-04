from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q  # Import Q object
from .models import Topic, Article

def home(request):
    topics = Topic.objects.all()
    most_viewed_articles = Article.objects.order_by('-views')[:5]
    return render(request, 'website/home.html', {
        'topics': topics,
        'most_viewed_articles': most_viewed_articles,
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'articles/article_detail.html', context)

def article_list(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'articles/article_list.html', {
        'topic': topic,
        'articles': topic.articles.all()
    })

def search(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))  # Search title and content
    else:
        articles = []  # No search query, return empty list

    return render(request, 'website/search_results.html', {'results': articles, 'query': query})