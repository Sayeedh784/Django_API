from django.db import models
from django.db.models.base import Model

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()

  def __str__(self):
    return self.title