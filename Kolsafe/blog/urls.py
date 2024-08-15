from django.urls import path
from blog.views import blog


urlpatterns = [
    path('listArticle/', blog, name='listArticle'),
]
