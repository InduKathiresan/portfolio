from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
    desc = models.TextField()


    def __str__(self):
        return self.name
