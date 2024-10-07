from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .models import Service, ContactService
from django.urls import reverse_lazy
from . forms import ContactServiceForm 




class ServiceListView(ListView):
    model = Service
    template_name = 'service/service_list.html'



class ServiceDetailView(FormMixin, DetailView):
    model = Service
    template_name = 'service/service_detail.html'
    form_class = ContactServiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_services'] = Service.objects.order_by('-created_at')[:5]
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
        form.instance.service = self.object
        form.save()
        return redirect('success')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class ServiceCreateView(CreateView):
    model = Service
    template_name = 'service/service_form.html'
    fields = ['title', 'description', 'price', 'image']

    def get_success_url(self):
        return reverse_lazy('service_detail', kwargs={'pk': self.object.pk})



def success_view(request):
    return render(request, "service/success.html")