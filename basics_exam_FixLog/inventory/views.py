from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Inventory
from .forms import AddItemForm, ItemUpdateForm


# Create your views here.

class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory'
    ordering = ['id']

class ItemDetailsView(DetailView):
    model = Inventory
    template_name = 'inventory/item_details.html'
    context_object_name = 'item'

class AddItemView(CreateView):
    model = Inventory
    form_class = AddItemForm
    template_name = 'inventory/add_item.html'
    success_url = reverse_lazy('inventory_list')

class ItemUpdateView(UpdateView):
    model = Inventory
    form_class = ItemUpdateForm
    template_name = "inventory/item_edit.html"
    context_object_name = "item"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("inventory_list")


class ItemDeleteView(DeleteView):
    model = Inventory
    template_name = "inventory/item_delete.html"
    context_object_name = "item"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("inventory_list")