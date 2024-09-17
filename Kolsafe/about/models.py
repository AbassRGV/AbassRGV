from django.db import models


# Create your models here.
class AboutDB(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email
