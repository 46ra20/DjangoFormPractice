from django.db import models

# Create your models here.
# First Name
# Last Name
# Email
# Phone number
# Instrument Type

class Musician(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=20)
    email=models.EmailField()
    phone = models.CharField(max_length=15)
    insType = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.fname