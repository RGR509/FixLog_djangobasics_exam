from django import forms

from .models import RepairTicket

class RepairTicketForm(forms.ModelForm):
    class Meta:
        model = RepairTicket
        fields = [
        'customer_name',
        'customer_phone',
        'device_type',
        'device_model',
        'reported_issue',
        'status',
        'cost',
        'technician',
        'parts_used',
        ]

    widgets = {
        'customer_name': forms.TextInput(attrs={
            'placeholder': 'Enter customer name',
        }),
        'customer_phone': forms.TextInput(attrs={
            'placeholder': 'Enter customer phone number',
        }),
        'device_type': forms.Select(),
        'device_model': forms.TextInput(attrs={
            'placeholder': 'e.g. Lenovo ThinkPad T14',
        }),
        'reported_issue': forms.Textarea(attrs={
            'placeholder': 'Describe the problem reported by the customer...',
            'rows': 4,
        }),
        'status': forms.Select(),
        'cost': forms.NumberInput(attrs={
            'placeholder': '0.00',
            'step': '0.01',
            'min': '0',
        }),
        'technician': forms.Select(),
        'parts_used': forms.CheckboxSelectMultiple(attrs={
            'size': 5,
        }),
    }

    labels = {
        'customer_name': 'Customer Name',
        'customer_phone': 'Customer Phone',
        'device_type': 'Device Type',
        'device_model': 'Device Model',
        'reported_issue': 'Reported Issue',
        'status': 'Repair Status',
        'cost': 'Repair Cost (€)',
        'technician': 'Assigned Technician',
        'parts_used': 'Spare Parts Used',
    }

class RepairTicketLookupForm(forms.Form):
    customer_name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={
            "placeholder": "Enter the customer name...",
        }),
    )

    customer_phone = forms.CharField(
        max_length=13,
        label="Phone Number",
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your phone number...",
        }),
    )