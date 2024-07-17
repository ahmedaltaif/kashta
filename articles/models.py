from django.db import models
from ckeditor.fields import RichTextField

class Topic(models.Model):
    """Represents a topic or category for articles."""

    title = models.CharField(max_length=200, default="", help_text='Enter the topic title.')  # Title of the topic
    logo = models.ImageField(upload_to='topic_logos/', blank=True, null=True)  # Add the logo field
    description = models.TextField(default='Default description', help_text='Enter the topic description.')  # Description of the topic
    content = models.TextField(default='Default content', help_text='Enter the topic content.')  # Content of the topic

    def __str__(self):
        return self.title

class Article(models.Model):

    """Represents an article related to a specific topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles', help_text='Select the topic for this article.')  # Topic related to the article
    title = models.CharField(max_length=200, default="", help_text='Enter the article title.')  # Title of the article
    summary = models.TextField(default='Default summary', help_text='Enter a summary for the article.')  # Summary of the article
    content = RichTextField(help_text='Enter the content of the article using Rich Text format.')  # Content of the article
    published_date = models.DateTimeField(auto_now_add=True, help_text='The date and time when the article was published.')  # Date and time of publication
    view_count = models.IntegerField(default=0, help_text='Number of times the article has been viewed.')  # Number of views for the article

    def __str__(self):
        return self.title
