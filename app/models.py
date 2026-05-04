from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Iten(models.Model):
    name = models.CharField(max_length=40)
    active = models.BooleanField(default=True)
    amount = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name




class Usuario(models.Model):
    user_name = models.CharField(max_length=60)
    phone = PhoneNumberField(default=0)  
    current_date = models.DateTimeField() 
    ordered_items = models.ManyToManyField(Iten, related_name='usuarios')
    
    def __str__(self):
        return self.user_name
