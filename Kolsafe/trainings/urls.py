from django.urls import path
from trainings.views import lesTrainings


urlpatterns = [
    path('listTraining/', lesTrainings, name='listTraining'),
]


