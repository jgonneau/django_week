from django.db import models

# Create your models here.

class Pokemon(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    comment = models.TextField(blank=True, default='')
