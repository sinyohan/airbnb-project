from typing import Tuple
from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models

# Create your models here.
class Room(core_models.TimeStampedModel):
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=140, null=True, blank=True)
    beds = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    baths = models.IntegerField(null=True, blank=True)
    guests = models.IntegerField(null=True, blank=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    instant_book = models.BooleanField(default=False, null=True, blank=True)
    host = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name
