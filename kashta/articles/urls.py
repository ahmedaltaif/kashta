from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('topic/<int:pk>/', views.article_list, name='article_list'),
    path('search/', views.search, name='search'),
]
