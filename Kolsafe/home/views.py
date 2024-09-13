from django.views.generic import TemplateView
from formation.models import Formation
from service.models import Service


class HomeView(TemplateView):
    template_name = 'home/home.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formations'] = Formation.objects.all()
        context['services'] = Service.objects.all()
        return context
