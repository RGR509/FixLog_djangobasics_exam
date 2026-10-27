from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models as m

# Create your models here.

class RepairTicket(m.Model):
    class DeviceType(m.TextChoices):
        PCS = "PCS", "PCs and Laptops"
        MOBILE_DEVICES = "MOBILE_DEVICES", "Mobile Devices"
        GAME_CONSOLES = "GAME_CONSOLES", "Game Consoles"
        TVS = "TVS", "TVs and Monitors"
        NETWORKING = "NETWORKING", "Networking Equipment"
        OTHER = "OTHER", "Other"

    class StatusChoices(m.TextChoices):
        RECEIVED = "RECEIVED", "Received"
        DIAGNOSING = "DIAGNOSING", "Diagnosing"
        WAITING_FOR_PARTS = "WAITING_FOR_PARTS", "Waiting for Parts"
        IN_REPAIR = "IN_REPAIR", "In Repair"
        COMPLETED = "COMPLETED", "Completed"
        DELIVERED = "DELIVERED", "Delivered"

    ticket_number = m.CharField(max_length=20, unique=True, null=True)
    customer_name = m.CharField(max_length=100)
    customer_phone = m.CharField(max_length=13)
    device_type = m.CharField(max_length=20, choices=DeviceType.choices)
    device_model = m.CharField(max_length=100)
    reported_issue = m.TextField()
    status = m.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.RECEIVED,
    )
    received_at = m.DateTimeField(auto_now_add=True)
    cost = m.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    technician = m.ForeignKey(
        "technicians.Technicians",
        on_delete=m.SET_NULL,
        null=True,
        related_name="repair_tickets",
    )
    parts_used = m.ManyToManyField(
        "inventory.Inventory",
        blank=True,
        related_name="repair_tickets",
    )

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            super().save(*args, **kwargs)
            self.ticket_number = f'TKT{self.pk:011d}'
            super().save(update_fields=['ticket_number'])
            return
        super().save(*args, **kwargs)

class Reviews(m.Model):
    author = m.CharField(max_length=100)
    rating = m.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(5.00)])
    body = m.TextField()
    repair_ticket = m.OneToOneField(
        "repairs.RepairTicket",
        on_delete=m.CASCADE,
        related_name='reviews'
    )
    technician = m.ForeignKey('technicians.Technicians', on_delete=m.CASCADE)
    created_at = m.DateTimeField(auto_now_add=True)
    is_verified = m.BooleanField(default=False)