from django import forms
from .models import Inventory

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ('sku_number',)
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Laptop SSD 1TB',
            }),
            'sku_number': forms.TextInput(attrs={
                'placeholder': 'Enter the 14-character SKU',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the spare part...',
                'rows': 4,
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
            }),
            'compatible_devices': forms.Select(),
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'Enter available quantity',
                'min': '0',
            }),
        }

class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ('sku_number',)
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Laptop SSD 1TB',
            }),
            'sku_number': forms.TextInput(attrs={
                'placeholder': 'Enter the 14-character SKU',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the spare part...',
                'rows': 4,
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
            }),
            'compatible_devices': forms.Select(),
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'Enter available quantity',
                'min': '0',
            }),
        }