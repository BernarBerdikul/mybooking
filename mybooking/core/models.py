from django.db import models
from mybooking.mixins.models import UpdateTimestampMixin, ValidateErrorMixin


class AllowedUser(ValidateErrorMixin):
    """ A class used to represent a User,
        who has access for bots commands """

    username = models.CharField(
        max_length=32, verbose_name="Логин пользователя в Telegram"
    )
    name = models.CharField(
        max_length=64, verbose_name="Имя пользователя в Telegram"
    )

    class Meta:
        db_table = "allowed_users"
        verbose_name = "Доступ пользователю"
        verbose_name_plural = "Доступ пользователям"

    def __str__(self):
        return f"{self.pk} - {self.username} - {self.name}"


class Room(UpdateTimestampMixin, ValidateErrorMixin):
    """ A class used to represent a Room entity """

    room_name = models.CharField(
        max_length=60, verbose_name="Название кабинета",
        unique=True, db_index=True
    )

    class Meta:
        db_table = "room"
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"

    def __str__(self):
        return f"{self.pk} - {self.room_name}"

    def save(self, *args, **kwargs):
        """ overwrite save method to save room_name with symbol '№' """
        if not self.room_name.startswith("№"):
            self.room_name = f"№{self.room_name}"
        """ before save"""
        super().save(*args, **kwargs)
        """ after save"""


class Booking(UpdateTimestampMixin, ValidateErrorMixin):
    """ A class used to represent a Booking entity """

    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="bookings",
        verbose_name="Кабинет"
    )
    user = models.ForeignKey(
        AllowedUser, on_delete=models.CASCADE,
        null=True, blank=True, related_name="bookings",
        verbose_name="Пользователь"
    )
    day = models.DateField(verbose_name="Дата бронирования")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время конца")

    class Meta:
        db_table = "booking"
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    def __str__(self):
        return f"{self.pk} - {self.start_time} - {self.end_time}"
