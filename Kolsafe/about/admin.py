from django.contrib import admin


# Register your models here.

from about.models import AboutDB


@admin.register(AboutDB)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message")
    
    # la valeur qui sera utilisée sur les champs vide dans la base de donnée.
    empty_value_display = "Champ vide"
