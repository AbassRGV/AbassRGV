from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField




class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='service/images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    
class ContactService(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    nomComplet = models.CharField(max_length=300)
    pays = CountryField()
    ville = models.CharField(max_length=200)
    tel_whatsapp = PhoneNumberField()
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
