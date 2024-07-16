from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Topic, Article

def home(request):
    latest_topics = Topic.objects.all()[:9]
    most_viewed_articles = Article.objects.order_by('-view_count')[:9]
    topics = Topic.objects.all()
    return render(request, 'website/home.html', {
        'latest_topics': latest_topics,
        'most_viewed_articles': most_viewed_articles,
        'topics': topics
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    topics = Topic.objects.all()
    template_name = 'articles/article_detail.html'
    context = {
        'article': article,
        'topics': topics
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        template_name = 'articles/article_detail_partial.html'
    return render(request, template_name, context)

def article_list(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    topics = Topic.objects.all()
    return render(request, 'articles/article_list.html', {
        'topic': topic,
        'articles': topic.articles.all(),
        'topics': topics
    })

def search(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        articles = []
    topics = Topic.objects.all()
    return render(request, 'website/search_results.html', {
        'results': articles,
        'query': query,
        'topics': topics
    })
