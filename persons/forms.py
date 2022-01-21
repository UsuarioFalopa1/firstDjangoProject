from django.forms import  ModelForm, EmailInput
from django.db import models
from persons.models import Person

#class Person(models.Model):
#    name = models.CharField(max_length = 255)
#    surname = models.CharField(max_length=255)
#    email = models.CharField(max_length=255)
    
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            'email' : EmailInput(attrs={'type':'email'})
        }