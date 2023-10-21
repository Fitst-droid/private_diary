from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
  """diary"""
  
  class Meta:
    verbose_name_plural = 'CustomUser'
  

