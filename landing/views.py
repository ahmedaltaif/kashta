from django.shortcuts import render
from articles.models import Topic, Article

def landing_page(request):
    topics = Topic.objects.all()
    return render(request, 'landing/landingpage.html', context)