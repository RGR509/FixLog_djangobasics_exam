from django.urls import path, include
from django.views import View

from .views import *

urlpatterns = [
    path('', TechniciansListView.as_view(), name='technicians_list'),
    path('register/', AddTechnicianView.as_view(), name='register_technician'),
    path('<int:pk>/', TechniciansDetailsView.as_view(), name='technician_details'),
    path("<int:pk>/edit/", TechnicianUpdateView.as_view(),name="technician_edit"),
    path("<int:pk>/delete/", TechnicianDeleteView.as_view(), name="technician_delete"),
]