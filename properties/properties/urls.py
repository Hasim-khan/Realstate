"""properties URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib.sitemaps.views import sitemap
from app1.sitemaps import BlogSitemap  
from app1.views import custom_sitemap_view
from app1 import views as app1_views
handler404 = app1_views.custom_404

sitemaps = {
    'blogs': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('sitemap.xml', custom_sitemap_view, name='sitemap'),
    
]
