from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from app1.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

class blog(View):
    def get(self, request):
        cdata = cmsblog.objects.all().order_by('id').reverse()
        return render(request, 'blog.html', {'cdata':cdata})