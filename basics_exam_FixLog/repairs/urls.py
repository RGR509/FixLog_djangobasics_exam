from django.urls import path, include

from repairs.views import RepairTicketCreateView
from .views import *

urlpatterns = [
    path('', RepairTicketCreateView.as_view(), name='request_repair'),
    path("<int:pk>/edit/", RepairTicketUpdateView.as_view(), name="repair_edit"),
    path("<int:pk>/delete/", RepairTicketDeleteView.as_view(), name="repair_delete"),
    path('my_tickets/', my_repair_tickets, name='my_repair_tickets'),
]