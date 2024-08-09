from django.urls import path
from contact.views import contact


urlpatterns = [
    path('listContact', contact, name='listContact'),
]
