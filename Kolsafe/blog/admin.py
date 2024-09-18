from django.contrib import admin

# Register your models here.
from blog.models import BlogDB


@admin.register(BlogDB)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "dateblog", "source", "img")

    # la valeur qui sera utilisée sur les champs vide dans la base de donnée.
    empty_value_display = "Champ vide"