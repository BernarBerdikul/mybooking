import os
from django.conf import settings


def get_restaurant_images(
    restaurant_id: int, filename: str, path="/", url=settings.SITE_URL
):
    return f"{url}{settings.MEDIA_URL}{restaurant_id}{path}{filename}"


def __files_unique_name(filename, new_filename: str):
    _, ext = os.path.splitext(filename.lower())
    return f"{new_filename}{ext}"


def image_room(instance, filename):
    return __files_unique_name(
        filename, new_filename=f"room_{instance.room_name}"
    )
