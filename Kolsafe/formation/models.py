from django.db import models


class Formation(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='formation/image', blank=True)
    description = models.TextField()
    certifier = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
