from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Formation
from django.urls import reverse_lazy


class FormationListView(ListView):
    model = Formation
    template_name = 'formation/formation_list.html'


class FormationDetailView(DetailView):
    model = Formation
    template_name = 'formation/formation_detail.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_formations'] = Formation.objects.order_by('-created_at')[:5]
        return context
    


class FormationCreateView(CreateView):
    model = Formation
    template_name = 'formation/formation_form.html'
    fields = ['title', 'image', 'description', 'price', 'certifier']


class FormationUpdateView(UpdateView):
    model = Formation
    template_name = 'formation/formation_form.html'
    fields = ['title', 'image', 'description', 'price', 'certifier']


class FormationDeleteView(DeleteView):
    model = Formation
    template_name = 'formation/formation_confirm_delete.html'
    success_url = reverse_lazy('formation_list')
