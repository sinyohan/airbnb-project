from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class TimeStampedModel(models.Model):
    created = DateTimeField(null=True, blank=True, auto_now_add=True)
    updated = DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        abstract = True
