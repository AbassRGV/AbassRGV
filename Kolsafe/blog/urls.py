from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from blog.views import BlogView, DetailBlogView

app_name = 'Blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<int:pk>/', DetailBlogView.as_view(), name='blogdetail'),
]