from django import forms

from blog.models import BlogDB


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogDB
        fields = ["title", "dateblog", "source", "img", "description", ]
