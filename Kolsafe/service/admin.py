from django.contrib import admin
from .models import Service, ContactService


class AdminService(admin.ModelAdmin):
    list_display = ['title', 'price', 'image', 'created_at', 'updated_at', 'publish_name']


admin.site.register(Service, AdminService)





class ContactServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'nomComplet', 'pays', 'ville', 'tel_whatsapp', 'email', 'message', 'created_at']


admin.site.register(ContactService, ContactServiceAdmin)