from django.db import models
from django.forms import CharField

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)