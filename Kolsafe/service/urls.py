from django.urls import path
from .views import ServiceListView, ServiceDetailView, ServiceCreateView
from . import views



urlpatterns = [
    path('', ServiceListView.as_view(), name='service_list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('new/', ServiceCreateView.as_view(), name='service_create'),
    path('success/', views.success_view, name='success'),

]
