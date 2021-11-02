from django.db import models
from core import models as core_models

# Create your models here.


class List(core_models.TimeStampedModel):

    name = models.CharField(max_length=80, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    rooms = models.ManyToManyField("rooms.Room", blank=True, null=True)

    def __str__(self):
        return self.name
