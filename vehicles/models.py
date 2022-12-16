from django.db import models
from django.db.models import CharField,DecimalField, Model
from django.db.models.fields.related import ForeignKey
#from django.mysql.models import ListCharField

import uuid

# Create your models here.

class Vehicle(models.Model):
    name            = models.CharField(max_length=200, null=True, blank=True)
    vin             = models.CharField(max_length=500, null=True, blank=True)
    van             = models.CharField(max_length=200, null=True, blank=True)
    location        = models.CharField(max_length=200, null=True, blank=True)
    mileage         = models.DecimalField(max_digits=10, decimal_places=2)
    comment         = models.CharField(max_length=200, null=True, blank=True)
    vehicle_image   = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profile/user-default.png')
    created         = models.DateTimeField(auto_now_add=True)
    id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Vehicle_Component(models.Model):

    vehicle         = models.OneToOneField(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    name            = models.CharField(max_length=200, null=True, blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name, self.vehicle)


