from django.contrib.auth.models import User
from django.db import models

from item.models import Item
# Create your models here.

class conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversation', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversation')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)