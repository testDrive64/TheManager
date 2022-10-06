from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.text

class Answer(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.text