from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.forms import BlogForm
from blog.models import BlogDB


class BlogView(ListView):
    model = BlogDB
    template_name = "blog/blog.html"
    context_object_name = "blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ggg'] = "gg"
        return context


class DetailBlogView(DetailView):
    model = BlogDB
    template_name = "blog/blogdetail.html"
    context_object_name = "blogdetail"
