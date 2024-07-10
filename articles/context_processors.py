from .models import Topic

def sidebar_topics(request):
    topics = Topic.objects.all()
    return {'topics': topics}