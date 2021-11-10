from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    address = models.TextField()