from django import forms
from .models import Technicians

class AddTechnicianForm(forms.ModelForm):
    class Meta:
        model = Technicians
        fields = [
            'name',
            'email',
            'phone',
            'speciality',
            'experience',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter technician name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@email.com',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter phone number',
            }),
            'speciality': forms.Select(),
            'experience': forms.NumberInput(attrs={
                'placeholder': 'Years of experience',
                'min': '3',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the technician’s skills and experience...',
                'rows': 4,
            }),
        }

class TechnicianUpdateForm(forms.ModelForm):
    class Meta:
        model = Technicians
        fields = [
            'name',
            'email',
            'phone',
            'speciality',
            'experience',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter technician name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@email.com',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter phone number',
            }),
            'speciality': forms.Select(),
            'experience': forms.NumberInput(attrs={
                'placeholder': 'Years of experience',
                'min': '3',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the technician’s skills and experience...',
                'rows': 4,
            }),
        }
