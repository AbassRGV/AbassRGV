from django.contrib import admin
from .models import Formation


class AdminFormation(admin.ModelAdmin):
    list_display = ['title', 'image', 'certifier', 'price', 'created_at', 'updated_at', 'publish_name']


admin.site.register(Formation, AdminFormation)
