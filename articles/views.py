from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Topic, Article

def home(request):
    """
    Renders the home page with the latest topics and most viewed articles.
    """
    latest_topics = Topic.objects.all()[:9]  # Get the latest 9 topics
    most_viewed_articles = Article.objects.order_by('-view_count')[:9]  # Get the 9 most viewed articles
    topics = Topic.objects.all()  # Get all topics for navigation
    return render(request, 'website/home.html', {
        'latest_topics': latest_topics,
        'most_viewed_articles': most_viewed_articles,
        'topics': topics
    })

def article_detail(request, pk):
    """
    Renders the detail view for a single article.
    """
    article = get_object_or_404(Article, pk=pk)  # Get the article by primary key or return a 404 error
    topics = Topic.objects.all()  # Get all topics for navigation
    template_name = 'articles/article_detail.html'  # Default template for article detail
    context = {
        'article': article,
        'topics': topics
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        template_name = 'articles/article_detail_partial.html'  # Use partial template for AJAX requests
    return render(request, template_name, context)

def article_list(request, pk):
    """
    Renders a list of articles for a specific topic.
    """
    topic = get_object_or_404(Topic, pk=pk)  # Get the topic by primary key or return a 404 error
    topics = Topic.objects.all()  # Get all topics for navigation
    return render(request, 'articles/article_list.html', {
        'topic': topic,
        'articles': topic.articles.all(),  # Get all articles related to the topic
        'topics': topics
    })

def search(request):
    """
    Renders the search results based on a query.
    """
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))  # Filter articles by title or content
    else:
        articles = []  # If no query, return an empty list
    topics = Topic.objects.all()  # Get all topics for navigation
    return render(request, 'website/search_results.html', {
        'results': articles,  # Search results
        'query': query,  # The search query
        'topics': topics
    })
