from django.contrib import admin
from .models import Formation


class AdminFormation(admin.ModelAdmin):
    list_display = ['title', 'image', 'description', 'certifier', 'price', 'created_at', 'updated_at']


admin.site.register(Formation, AdminFormation)
