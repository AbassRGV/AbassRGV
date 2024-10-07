from django import forms
from .models import InscriptionF



class InscriptionForm(forms.ModelForm):
    class Meta:
        model = InscriptionF
        fields = ['nomComplet', 'tel_whatsapp', 'email', 'message' ]
        widgets = {
            'nomComplet': forms.TextInput(attrs={'class': 'form-control'}),
            'tel_whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
