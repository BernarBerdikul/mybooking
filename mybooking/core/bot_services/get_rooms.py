from django.db.models import Prefetch
from ..models import (
    Room, Booking
)
from telebot import types
from datetime import datetime, date
from ...utils import constants


def get_rooms() -> types.InlineKeyboardMarkup:
    now = datetime.now().time().strftime("%H:%M:%S")
    today = date.today()
    markup = types.InlineKeyboardMarkup(row_width=2)
    rooms = Room.objects.prefetch_related(
        Prefetch(
            "bookings",
            queryset=Booking.objects.filter(
                day=today, start_time__lt=now, end_time__gt=now
            ),
            to_attr="room_bookings",
        ),
    ).all()
    for room in rooms:
        """ prepare visual text """
        if room.room_bookings:
            username = room.room_bookings[0].username
            is_booked = f"Занято - {username}"
        else:
            is_booked = "Свободно"
        text = f"{room.room_name} {is_booked}"
        """ add in InlineKeyboard """
        markup.add(
            types.InlineKeyboardButton(
                text=text, callback_data=room.room_name
            ),
            types.InlineKeyboardButton(
                text=constants.ROOM_INFO,
                callback_data=f"{constants.ROOM_INFO} - {room.room_name}"
            )
        )
    return markup
