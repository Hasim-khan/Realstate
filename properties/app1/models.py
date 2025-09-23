from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.urls import reverse
# Create your models here.

class cmsblog(models.Model):
    image=models.ImageField(upload_to='media', null=True)
    title=models.CharField(max_length=100 , null=True , blank=False)
    content=RichTextField()
    blogdate= models.DateTimeField(default=timezone.now)
    blog_title = AutoSlugField(populate_from='title', unique=True, null=True, blank=False)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogdetail", args=[self.blog_title])

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    service_type = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"