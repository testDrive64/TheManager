from typing import BinaryIO
from django.db import models
from django.db.models import CharField, Model
from django.db.models.fields.related import ForeignKey
#from django.mysql.models import ListCharField

from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name            = models.CharField(max_length=200, null=True, blank=True)
    email           = models.EmailField(max_length=500, null=True, blank=True)
    username        = models.CharField(max_length=200, null=True, blank=True)
    location        = models.CharField(max_length=200, null=True, blank=True)
    short_intro     = models.CharField(max_length=200, null=True, blank=True)
    bio             = models.TextField(null=True, blank=True)
    profile_image   = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profile/user-default.png')
    social_github   = models.CharField(max_length=200, null=True, blank=True)
    social_twitter  = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_youtube  = models.CharField(max_length=200, null=True, blank=True)
    social_website  = models.CharField(max_length=200, null=True, blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner       = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name        = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    id          = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class School(models.Model):
    name        = models.CharField(max_length=200, null=True, blank=True)
    address     = models.CharField(max_length=200, null=True, blank=True)
    bio         = models.TextField(null=True, blank=True)
    president   = models.CharField(max_length=200, null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    id          = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Grade(models.Model):
    school      = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    number      = models.IntegerField(null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    id          = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.owner.name + ", Grade: " + self.number)

class Certification(models.Model):
    name    = models.CharField(max_length=200, null=True, blank=True)
    grade   = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    mark = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id      = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Education(models.Model):
    owner          = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    #schools        = models.ListCharField(base_field=ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True), null=True, blank=True)
    #certifications = models.ListCharField(base_field=ForeignKey(Certification, on_delete=models.CASCADE, null=True, blank=True))
    currentState   = models.CharField(max_length=200, null=True, blank=True)
    created        = models.DateTimeField(auto_now_add=True)
    id             = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.currentState)


#class Mediathek(models.Model):
#    music_dict = models.DataField()
