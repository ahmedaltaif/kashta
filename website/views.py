from django.shortcuts import render
from articles.models import Topic, Article

def home(request):
    latest_topics = Topic.objects.all()[:6]
    most_viewed_articles = Article.objects.order_by('-view_count')[:6]
    return render(request, 'website/home.html', {
        'latest_topics': latest_topics,
        'most_viewed_articles': most_viewed_articles,
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.is_ajax():
        data = {
            'title': article.title,
            'content': article.content,
        }
        return JsonResponse(data)
    return render(request, 'articles/article_detail.html', {'article': article})
# Optional search functionality (replace with your desired logic)




def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Article.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    return render(request, 'website/search_results.html', {'query': query, 'results': results})