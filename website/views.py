from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from articles.models import Topic, Article

def home(request):
    """
    Renders the home page with the latest topics and most viewed articles.
    """
    latest_topics = Topic.objects.all()[:6]  # Get the latest 6 topics
    most_viewed_articles = Article.objects.order_by('-view_count')[:6]  # Get the 6 most viewed articles
    return render(request, 'website/home.html', {
        'latest_topics': latest_topics,
        'most_viewed_articles': most_viewed_articles,
    })

def article_detail(request, pk):
    """
    Renders the detail view for a single article.
    """
    article = get_object_or_404(Article, pk=pk)  # Get the article by primary key or return a 404 error
    if request.is_ajax():  # Check if the request is an AJAX request
        data = {
            'title': article.title,
            'content': article.content,
        }
        return JsonResponse(data)  # Return article data as JSON for AJAX requests
    return render(request, 'articles/article_detail.html', {'article': article})  # Render the article detail template

def search(request):
    """
    Renders the search results based on a query.
    """
    query = request.GET.get('q')  # Get the search query from the request
    results = []
    if query:
        results = Article.objects.filter(
            Q(title__icontains=query) |  # Filter articles by title containing the query
            Q(content__icontains=query)  # Filter articles by content containing the query
        )
    return render(request, 'website/search_results.html', {'query': query, 'results': results})  # Render search results
