from django.db import models

# Create your models here.

class channel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    idChannel = models.CharField(max_length=100)
    idUser = models.CharField(max_length=100)
    comment = models.TextField(blank=True, default='')
