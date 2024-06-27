from django.db import models
from django.utils import timezone

class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles', default=1)  # Assuming a Topic with ID 1 exists
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)  # Use default instead of auto_now_add
    def __str__(self):
        return self.title
