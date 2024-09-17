from django.db import models

# Create your models here.
from django.utils.timezone import now


class BlogDB(models.Model):
    title = models.CharField(max_length=100, blank=False)
    dateblog = models.DateField(null=True, blank=True)
    source = models.CharField(max_length=100,)
    img = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
