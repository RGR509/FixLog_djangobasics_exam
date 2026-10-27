from decimal import Decimal

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models as m


# Create your models here.

class Inventory(m.Model):
    class CompatibleDevices(m.TextChoices):
        PCS = "PCS", "PCs and Laptops"
        MOBILE_DEVICES = "MOBILE_DEVICES", "Mobile Devices"
        GAME_CONSOLES = "GAME_CONSOLES", "Game Consoles"
        TVS = "TVS", "TVs and Monitors"
        NETWORKING = "NETWORKING", "Networking Equipment"
        GENERAL_ELECTRONICS = "GENERAL_ELECTRONICS", "General Electronics"

    name = m.CharField(max_length=100)
    sku_number = m.CharField(max_length=14, unique=True, validators=[MinLengthValidator(14)])
    description = m.TextField()
    price = m.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    compatible_devices = m.CharField(max_length=50, choices=CompatibleDevices.choices)
    quantity = m.PositiveIntegerField()
    created_at = m.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.sku_number:
            super().save(*args, **kwargs)
            self.sku_number = f'FIX{self.pk:011d}'
            super().save(update_fields=['sku_number'])
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'