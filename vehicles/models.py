from enum import Enum
from typing import BinaryIO
from django.db import models
from django.db.models import FloatField, CharField, Model
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

from users.models import Profile

import uuid

class Vehicle(models.Model):
    name = models.CharField(max_length=20)
    vin = models.CharField(max_length=10)
    van = models.CharField(max_length=10)
    vehType = models.CharField(max_length=15, null=True, blank=True)
    axleConfig = models.CharField(max_length=5, default="4x2")
    comment = models.CharField(max_length=100)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta():
        ordering: ['created']

class MileageType(models.TextChoices):
    Markbronn = "Markbronn"
    Vehicle = "Vehicle"

class MileageItem(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    mileage = models.FloatField()
    mileageType = models.CharField(max_length=10, choices=MileageType.choices)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.mileage) + " km, " + self.mileageType

class Powersource(models.TextChoices):
    Diesel = "Diesel"
    Benzin = "Benzin"
    CNG = "CNG"
    LNG = "LNG"
    H2 = "H2"
    kwh = "kwh"

class Fueling(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    powersource = models.CharField(max_length=7, choices=Powersource.choices) #:[(source, source.value) for source in Powersource])
    litre = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.powersource) + " " + str(self.litre)

class StatusLocation(models.TextChoices):
    Running = "Running"
    IvecoFacility = "IvecoFacility"

class MissionType(models.TextChoices):
    LoongRun = "LongRun"
    Prototype = "Prototype"
    SpecialSensor = "SpecialSensor"
    Level4 = "Level4"

class Mission(models.Model):
    name = models.CharField(max_length=30)
    targetMileage = models.FloatField()
    groupMission = models.CharField(max_length=15, choices=MissionType.choices)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name + ", " + self.groupMission

class Customer(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    registration = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    location = models.CharField(max_length=15)
    locationStatus = models.CharField(max_length=15, choices=StatusLocation.choices)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name + " " + self.location

class VM_Component(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    component = models.ForeignKey(Component, on_delete=models.CASCADE, nill=True, blank=True)
    install_mileage = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.component
