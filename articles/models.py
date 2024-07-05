from django.db import models
from ckeditor.fields import RichTextField

class Topic(models.Model):
    title = models.CharField(max_length=200, default="")
    description = models.TextField(default='Default description')  # Add description field
    content = models.TextField(default='Default content')  # Add default value

    def __str__(self):
        return self.title

class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles', )
    title = models.CharField(max_length=200, default="")
    summary = models.TextField(default='Default summary')
    content = RichTextField()
    published_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
