from django.db import models

class Contact(models.Model):
    # from dataset
    name = models.CharField(max_length=200)          # "Doctor Name"
    education = models.CharField(max_length=300, blank=True)
    speciality = models.CharField(max_length=200)    # "Speciality"
    experience = models.IntegerField(default=0)      # years from "Experience"
    address = models.CharField(max_length=300)       # "Address"
    city = models.CharField(max_length=200)          # "Location"

    # extra fields for recommendation / app
    fees = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.speciality})"

