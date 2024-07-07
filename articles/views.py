from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Topic, Article

def home(request):
    latest_topics = Topic.objects.all()[:6]
    most_viewed_articles = Article.objects.order_by('-view_count')[:6]
    topics = Topic.objects.all()
    return render(request, 'website/home.html', {
        'latest_topics': latest_topics,
        'most_viewed_articles': most_viewed_articles,
        'topics': topics
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})

def article_list(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'articles/article_list.html', {
        'topic': topic,
        'articles': topic.article_set.all()
    })

def search(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        articles = []
    return render(request, 'website/search_results.html', {'results': articles, 'query': query})
