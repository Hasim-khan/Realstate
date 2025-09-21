from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    path('', views.index, name='home'), 
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog.as_view(), name='blog'),
    path('services/', views.services, name='services'),
    path('properties/', views.properties, name='properties'),

    #contact form
    path("contactform/", views.contact_form_view, name="contactform"),
    path("thank-you/", views.thank_you_view, name="thank_you"),

    # Example
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),


]