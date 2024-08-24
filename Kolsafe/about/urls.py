from django.urls import path
from about.views import about

app_name = "About"

urlpatterns = [
    path('', about, name='about'),
]
