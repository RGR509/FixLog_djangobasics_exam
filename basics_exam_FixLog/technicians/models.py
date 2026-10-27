from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models as m
from decimal import Decimal

from django.template.defaultfilters import lower


# Create your models here.

class Technicians(m.Model):
    class SpecialityChoices(m.TextChoices):
        PCS = "PCS", "PCs and Laptops"
        MOBILE_DEVICES = "MOBILE_DEVICES", "Mobile Devices"
        GAME_CONSOLES = "GAME_CONSOLES", "Game Consoles"
        TVS = "TVS", "TVs and Monitors"
        NETWORKING = "NETWORKING", "Networking Equipment"
        DATA_RECOVERY = "DATA_RECOVERY", "Data Recovery"
        HARDWARE = "HARDWARE", "General Hardware Repair"
        SOFTWARE = "SOFTWARE", "Software and Operating Systems"
        GENERAL = "GENERAL", "General Electronics"

    name = m.CharField(max_length=200)
    email = m.EmailField()
    phone = m.CharField(max_length=13)
    speciality = m.CharField(max_length=200, choices=SpecialityChoices.choices)
    experience = m.PositiveIntegerField(validators=[MinValueValidator(3)])
    description = m.TextField(default='No description provided.')
    rating = m.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(Decimal('5.00'))], default=Decimal('0.00'))
    member_since = m.DateTimeField(auto_now_add=True)
    verified = m.BooleanField(default=False)
    is_available = m.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {' '.join(self.speciality.split('_')).lower().capitalize()}'

