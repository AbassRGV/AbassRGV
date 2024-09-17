from django.urls import path
from about.views import AboutView

app_name = "About"

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]
