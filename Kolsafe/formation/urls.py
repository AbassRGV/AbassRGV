from django.urls import path
from .views import FormationListView, FormationDetailView, FormationCreateView, FormationUpdateView, FormationDeleteView

urlpatterns = [
    path('', FormationListView.as_view(), name='formation_list'),
    path('<int:pk>/', FormationDetailView.as_view(), name='formation_detail'),
    path('new/', FormationCreateView.as_view(), name='formation_create'),
    path('<int:pk>/edit/', FormationUpdateView.as_view(), name='formation_update'),
    path('<int:pk>/delete/', FormationDeleteView.as_view(), name='formation_delete'),
]
