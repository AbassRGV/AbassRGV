from django.urls import path
from .views import FormationListView, FormationDetailView, FormationCreateView
from . import views

urlpatterns = [
    path('', FormationListView.as_view(), name='formation_list'),
    path('<int:pk>/', FormationDetailView.as_view(), name='formation_detail'),
    path('new/', FormationCreateView.as_view(), name='formation_create'),
    path('successF/', views.success_view, name='successF'),
    
]
