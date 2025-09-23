from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from app1.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import sweetify
from django.shortcuts import render, get_object_or_404
# Create your views here.

from django.contrib.sitemaps import Sitemap
from app1.sitemaps import BlogSitemap

sitemaps = {
    'blogs': BlogSitemap,
}
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

class blog(View):
    def get(self, request):
        cdata = cmsblog.objects.all().order_by('id').reverse()
        return render(request, 'Blog/blog-grid.html', {'cdata':cdata})
    
class blogdetail(View):
    def get(self,request,slug):
        blogdata = cmsblog.objects.get(blog_title=slug)
        return render(request,'Blog/blog-detail.html', {'blogdata':blogdata})
    
def services(request):
    return render(request, 'our-service.html')

def properties(request):
    return render(request, 'property-halfmap-grid.html')


def contact_form_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        service_type = request.POST.get("service_type")
        message = request.POST.get("message")

        # Save to DB
        contact = ContactMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            service_type=service_type,
            message=message,
        )
        contact.save()
        # Send thank you email to user with your custom HTML template
        subject = "Thank you for contacting us!"
        email_html = render_to_string("Thankyoumail/email.html", {'first_name': first_name})
        email_text = strip_tags(email_html)  # Plain text fallback
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, email_text, from_email, [email], html_message=email_html)

        sweetify.success(request, 'Hey!!!', text='We Will Contact You Soon!', persistent='Done')
        return redirect("contactform")

    return render(request, "contact.html")

def thank_you_view(request):
    return render(request, "thank_you.html")

def Privacy_Policy(request):
    return render(request,"privacy-policy.html")



def human_sitemap(request):
    posts = cmsblog.objects.all().order_by('-blogdate')
    return render(request, 'sitemaps/sitemap.html', {'posts': posts})

def custom_sitemap_view(request):
    response = HttpResponse(content_type='application/xml')
    response.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    response.write('<?xml-stylesheet type="text/xsl" href="/static/sitemap.xsl"?>\n')
    response.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url in sitemaps['blogs']().items():
        response.write(f'<url>\n')
        response.write(f'  <loc>{url.get_absolute_url()}</loc>\n')
        response.write(f'  <lastmod>{url.blogdate}</lastmod>\n')
        response.write(f'  <changefreq>weekly</changefreq>\n')
        response.write(f'  <priority>0.8</priority>\n')
        response.write('</url>\n')
    response.write('</urlset>\n')
    return response