from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    CURRENCY_USD = "usd"
    CURRENCY_KR = "krw"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KR, "KRW"))
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars")
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=10, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
