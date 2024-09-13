from django.contrib import admin
from .models import Service


class AdminService(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'image', 'created_at', 'updated_at', 'publish_name']


admin.site.register(Service, AdminService)
