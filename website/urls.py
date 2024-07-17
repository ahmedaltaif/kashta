from django.urls import path  # Import the 'path' function from django.urls
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Home page view
    path('search/', views.search, name='search'),  # Search view
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # Article detail view
]
