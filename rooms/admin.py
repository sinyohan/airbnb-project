from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Tbumbnail"


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Spaces",
            {"fields": ("baths", "guests", "beds", "bedrooms")},
        ),
        (
            "More About the Spaces",
            {"fields": ("amenity", "facility", "house_rule"), "classes": ("collapse",)},
        ),
        ("Last Details", {"fields": ("host",)}),
    )
    list_display = (
        "name",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    list_filter = (
        "instant_book",
        "city",
        "host__superhost",
        "room_type",
        "amenity",
        "facility",
        "house_rule",
        "country",
    )
    # ordering = ("name", "guests")
    search_fields = ("=city", "^host__username")

    filter_horizontal = ("amenity", "facility", "house_rule")

    def count_amenities(self, obj):
        return obj.amenity.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_amenities.short_description = "hello sexy!"


# Register your models here.
