from django.shortcuts import render

from about.forms import AboutForm


def about(request):
    form = AboutForm()
    # about_click a verifié pour afficher ou cacher le boutton Contact
    about_click = True
    return render(request, 'about/about.html', {"form": form, "about_click": about_click})
