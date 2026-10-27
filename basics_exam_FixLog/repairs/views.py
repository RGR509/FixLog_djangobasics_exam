from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import RepairTicketForm, RepairTicketLookupForm
from .models import RepairTicket

class RepairTicketCreateView(CreateView):
    model = RepairTicket
    form_class = RepairTicketForm
    template_name = 'repairs/repair_ticket_create.html'
    success_url = reverse_lazy('my_repair_tickets')

from django.shortcuts import render

from .forms import RepairTicketLookupForm
from .models import RepairTicket


def my_repair_tickets(request):
    tickets = RepairTicket.objects.none()
    searched = False
    deleted = False

    if request.method == "POST":
        form = RepairTicketLookupForm(request.POST)

        if form.is_valid():
            searched = True

            name = form.cleaned_data["customer_name"].strip()
            phone = form.cleaned_data["customer_phone"].strip()

            if "delete_ticket" in request.POST:
                ticket_id = request.POST.get("delete_ticket")

                ticket = RepairTicket.objects.filter(
                    pk=ticket_id,
                    customer_name__iexact=name,
                    customer_phone=phone,
                ).first()

                if ticket:
                    ticket.delete()
                    deleted = True

            tickets = (
                RepairTicket.objects
                .filter(
                    customer_name__iexact=name,
                    customer_phone=phone,
                )
                .select_related("technician")
                .prefetch_related("parts_used")
                .order_by("-received_at")
            )
    else:
        form = RepairTicketLookupForm()

    return render(
        request,
        "repairs/repairs_by_name_form.html",
        {
            "form": form,
            "tickets": tickets,
            "searched": searched,
            "deleted": deleted,
        },
    )

class RepairTicketUpdateView(UpdateView):
    model = RepairTicket
    form_class = RepairTicketForm
    template_name = "repairs/repair_ticket_edit.html"
    context_object_name = "repair"
    success_url = reverse_lazy("repairs_list")

class RepairTicketDeleteView(DeleteView):
    model = RepairTicket
    template_name = "repairs/repair_ticket_delete.html"
    context_object_name = "repair"
    success_url = reverse_lazy("repairs_list")