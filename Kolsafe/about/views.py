from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from about.forms import AboutForm
from about.models import AboutDB


class AboutView(CreateView):
    model = AboutDB
    template_name = "about/about.html"
    form_class = AboutForm
    success_url = reverse_lazy("About:about")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_click = True
        context['about_click'] = about_click
        return context


