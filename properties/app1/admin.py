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


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3  # Default 3 image upload slots
    max_num = 10  # Optional max images

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]
    list_display = ('title', 'location', 'price', 'status', 'created_at')
    list_filter = ('status', 'location', 'created_at')
    search_fields = ('title', 'location')