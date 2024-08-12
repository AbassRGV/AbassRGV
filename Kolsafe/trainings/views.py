from django.shortcuts import render

def lesTrainings(request):
    return render(request, 'training/listTraining.html')
