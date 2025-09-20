from django.contrib import admin
from app1.models import *
# Register your models here.

@admin.register(cmsblog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'date',
    ]
    list_display = ['title','content','image','blogdate']