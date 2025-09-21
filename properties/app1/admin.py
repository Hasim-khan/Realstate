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


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "service_type", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone", "service_type")