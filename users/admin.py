from django.contrib import admin
from . import models

from django.contrib.auth.admin import UserAdmin

# 그냥 admin을 써서 admin.ModelAdmin을 하면 그냥 평버하게 뜨고
# UserAdmin을 쓰면 좀 더 깔끔하고 정리정돈 되게 쓸 수 있다
# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User admin"""

    # pass
    fieldsets = UserAdmin.fieldsets + (
        (
            "my custom filed",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
