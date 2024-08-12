from django.shortcuts import render




def lesServices(request):
    return render(request, 'services/listServices.html')
