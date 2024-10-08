from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField



class Formation(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='formation/image', blank=True)
    description = models.TextField()
    certifier = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class InscriptionF(models.Model):
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE)
    nomComplet = models.CharField(max_length=300)
    tel_whatsapp = PhoneNumberField()
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    


