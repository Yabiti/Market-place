from django.contrib.auth import User
from django.db import models

from item.models import Item
# Create your models here.

class conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversation', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversation')