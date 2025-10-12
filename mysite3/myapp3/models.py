from django.db import models

class Contact(models.Model):
    # id field is auto-added by Django as a primary key
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=200, blank=True)
    profession = models.CharField(max_length=120, blank=True)
    tel_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

# Create your models here.
