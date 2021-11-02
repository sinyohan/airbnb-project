from typing import Tuple
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    pass

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    pass

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80, null=True, blank=True)
    file = models.ImageField(null=True, blank=True)
    room = models.ForeignKey("Room", on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    name = models.CharField(
        max_length=120,
        null=True,
    )
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
        "users.User", on_delete=models.CASCADE, null=True, blank=True
    )
    room_type = models.ForeignKey(
        "RoomType", on_delete=models.SET_NULL, blank=True, null=True
    )
    amenity = models.ManyToManyField("Amenity", blank=True, null=True)
    facility = models.ManyToManyField("Facility", blank=True, null=True)
    house_rule = models.ManyToManyField("HouseRule", blank=True, null=True)

    def __str__(self):
        return self.name
