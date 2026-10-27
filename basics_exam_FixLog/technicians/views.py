from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Technicians
from .forms import AddTechnicianForm, TechnicianUpdateForm


# Create your views here.

class TechniciansListView(ListView):
    model = Technicians
    template_name = 'technicians/technicians_list.html'
    context_object_name = 'technicians'
    ordering = ['id']

class TechniciansDetailsView(DetailView):
    template_name = 'technicians/technician_details.html'
    model = Technicians
    context_object_name = 'technician'

class AddTechnicianView(CreateView):
    model = Technicians
    form_class = AddTechnicianForm
    template_name = 'technicians/technician_add.html'
    success_url = reverse_lazy('technicians_list')


class TechnicianUpdateView(UpdateView):
    model = Technicians
    form_class = TechnicianUpdateForm
    template_name = "technicians/technician_edit.html"
    context_object_name = "technician"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("technicians_list")


class TechnicianDeleteView(DeleteView):
    model = Technicians
    template_name = "technicians/technician_delete.html"
    context_object_name = "technician"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("technicians_list")