from django.urls import path
from blog.views import blog

app_name = 'Blog'

urlpatterns = [
    path('', blog, name='blog'),
]
