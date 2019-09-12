from django.db import models

# Create your models here.

class userMessage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    pseudo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
