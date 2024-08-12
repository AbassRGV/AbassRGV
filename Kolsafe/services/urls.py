from django.urls import path
from services.views import lesServices


urlpatterns = [
    path('listServices/', lesServices, name='listServices'),
]
