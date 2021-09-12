from django.db.models import Prefetch
from ..models import (
    Room, Booking
)
from telebot import types
from datetime import datetime


def get_time_periods(room: str) -> types.InlineKeyboardMarkup:
    now = datetime.now().time().strftime("%H:%M:%S")
    markup = types.InlineKeyboardMarkup(row_width=1)
    return markup
