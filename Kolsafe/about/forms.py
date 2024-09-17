from django import forms

from about.models import AboutDB


class AboutForm(forms.ModelForm):
    class Meta:
        model = AboutDB
        fields = ["name", "email", "subject", "message", ]
