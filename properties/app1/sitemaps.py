# app1/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import cmsblog

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return cmsblog.objects.all()

    def lastmod(self, obj):
        return obj.blogdate
