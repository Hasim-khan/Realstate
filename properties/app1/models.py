from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
# Create your models here.

class cmsblog(models.Model):
    image=models.ImageField(upload_to='media', null=True)
    title=models.CharField(max_length=100 , null=True , blank=False)
    content=RichTextField()
    blogdate= models.DateTimeField(default=timezone.now)
    blog_title = AutoSlugField(populate_from='title', unique=True, null=True, blank=False)