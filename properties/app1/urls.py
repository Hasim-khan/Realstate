from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
# from app1.sitemaps import BlogSitemap
# sitemaps = {
#     'blog': BlogSitemap,
# }

urlpatterns = [
    path('', views.index, name='home'), 
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    #Blogs
    path('blog/', views.blog.as_view(), name='blog'),
    path('blogdetail/<slug>',views.blogdetail.as_view(), name='blogdetail'),
    #site map
    path('sitemap/', views.human_sitemap, name='human_sitemap'),

    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('services/', views.services, name='services'),
    #cms for property
    path('properties/', views.properties.as_view(), name='properties'),
    path('property_detail/<slug>', views.property_detail.as_view(), name='property_detail'),
    #contact form
    path("contactform/", views.contact_form_view, name="contactform"),
    path("thank-you/", views.thank_you_view, name="thank_you"),
    path("Privacy_Policy/", views.Privacy_Policy, name="Privacy_Policy"),
    # path("error_page/", views.custom_404_view, name="error_404"),
    # Example
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),


]