from mybooking.core.models import AllowedUser
from telebot import types


def get_users(
        username: str,
        new_booking_object_id: int
) -> types.InlineKeyboardMarkup:
    users = AllowedUser.objects.all()
    markup = types.InlineKeyboardMarkup(row_width=2)
    for user in users:
        """ add in InlineKeyboard """
        if user.username == username:
            text = "На себя"
        else:
            text = user.name
        callback_data = user.id
        markup.add(
            types.InlineKeyboardButton(
                text=text, callback_data=f"-@ {callback_data} - {new_booking_object_id}"
            )
        )
    return markup
