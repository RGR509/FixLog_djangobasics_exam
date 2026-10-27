from django.urls import path, include
from .views import *

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory_list'),
    path('add/', AddItemView.as_view(), name='add_item'),
    path("<int:pk>/edit/", ItemUpdateView.as_view(), name="item_edit"),
    path("<int:pk>/delete/", ItemDeleteView.as_view(), name="item_delete"),
    path('<int:pk>/', ItemDetailsView.as_view(), name='item_details')
]