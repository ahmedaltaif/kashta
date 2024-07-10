"""kashta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),  # Include website URLs
    path('articles/', include('articles.urls')),  # Include articles URLs
    path('landingpage/', include('landing.urls')),  # Replace with your landing page URL configuration,
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "kastha knowledge base"
admin.site.site_header = "kashta admin"
admin.site.site_title = "kashta admin"