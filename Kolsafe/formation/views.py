from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from .forms import InscriptionForm
from .models import Formation, InscriptionF
from django.urls import reverse_lazy


class FormationListView(ListView):
    model = Formation
    template_name = 'formation/formation_list.html'


class FormationDetailView(FormMixin, DetailView):
    model = Formation
    template_name = 'formation/formation_detail.html'
    form_class = InscriptionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_formations'] = Formation.objects.order_by('-created_at')[:5]
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.formation = self.object
        form.save()
        return redirect('successF')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_formations'] = Formation.objects.order_by('-created_at')[:5]
        return context
    


class FormationCreateView(CreateView):
    model = Formation
    template_name = 'formation/formation_form.html'
    fields = ['title', 'image', 'description', 'price', 'certifier']


def success_view(request):
    return render(request, "formation/successF.html")
