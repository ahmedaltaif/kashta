from django.shortcuts import render

# Create your views here.
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})
