from django.contrib import admin
from .models import Formation, InscriptionF


class AdminFormation(admin.ModelAdmin):
    list_display = ['title', 'image', 'certifier', 'price', 'created_at', 'updated_at', 'publish_name']

admin.site.register(Formation, AdminFormation)


class AdminInscriptionF(admin.ModelAdmin):
    list_display = ['formation', 'nomComplet', 'tel_whatsapp', 'email', 'message' ]

admin.site.register(InscriptionF, AdminInscriptionF)
