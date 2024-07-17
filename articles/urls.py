from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # Detail view of a specific article
    path('topic/<int:pk>/', views.article_list, name='article_list'),  # List view of articles under a specific topic
    path('search/', views.search, name='search'),  # Search functionality
]
