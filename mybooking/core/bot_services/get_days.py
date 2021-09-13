from telebot import types
from datetime import date, timedelta
from ...utils import constants


def get_days(room_name: str) -> types.InlineKeyboardMarkup:
    now = date.today()
    markup = types.InlineKeyboardMarkup()
    for day in range(7):
        """ add in InlineKeyboard """
        w_day = now + timedelta(days=day)
        if w_day.weekday() in range(5):
            if now == w_day:
                text = "Сегодня"
                callback_data = f"{constants.DAYS_OF_THE_WEEK[w_day.weekday()]} - " \
                       f"{room_name} - {w_day.strftime('%d-%m-%Y')}"
            else:
                text = f"{constants.DAYS_OF_THE_WEEK[w_day.weekday()]} - " \
                       f"{room_name} - {w_day.strftime('%d-%m-%Y')}"
                callback_data = f"{constants.DAYS_OF_THE_WEEK[w_day.weekday()]} - " \
                       f"{room_name} - {w_day.strftime('%d-%m-%Y')}"
            markup.add(
                types.InlineKeyboardButton(
                    text=text, callback_data=callback_data
                )
            )
    return markup
