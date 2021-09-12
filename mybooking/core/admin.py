from django.contrib import admin
from .models import (
    Room,
    Booking,
    AllowedUser
)
from ..mixins.paginator import LargeTablePaginator
from ..utils import constants
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(AllowedUser)
class AllowedUserAdmin(admin.ModelAdmin):
    """ A class used to represent a AllowedUser model in admin page """

    list_display = ["id", "username", "name"]
    list_display_links = ["id", "username", "name"]
    fields = ("username", "name")
    search_fields = ("id", "username", "name")
    list_per_page = constants.OBJECTS_PER_PAGE_IN_ADMIN
    paginator = LargeTablePaginator


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """ A class used to represent a Room model in admin page """

    list_display = ["id", "room_name"]
    list_display_links = ["id", "room_name"]
    fields = ("room_name",)
    search_fields = ("id", "room_name")
    list_per_page = constants.OBJECTS_PER_PAGE_IN_ADMIN
    paginator = LargeTablePaginator


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ A class used to represent a Room model in admin page """

    list_display = [
        "id", "room", "username", "day", "start_time", "end_time"
    ]
    list_display_links = [
        "id", "room", "username", "day", "start_time", "end_time"
    ]
    fields = ("room", "username", "day", "start_time", "end_time")
    search_fields = ("id", "room_name", "username")
    list_per_page = constants.OBJECTS_PER_PAGE_IN_ADMIN
    paginator = LargeTablePaginator
