from django.db import models

# Create your models here.
class Category(models.model):
    name = models.CharField(max_length=255)