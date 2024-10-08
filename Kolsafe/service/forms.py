from django import forms
from .models import ContactService



class ContactServiceForm(forms.ModelForm):
    class Meta:
        model = ContactService
        fields = ['pays', 'ville', 'tel_whatsapp', 'email', 'message']
        widgets = {
            'pays': forms.Select(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'tel_whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactServiceForm, self).__init__(*args, **kwargs)
        self.fields['pays'].initial = 'GN'  # Code ISO 3166-1 alpha-2 pour la Guinée
