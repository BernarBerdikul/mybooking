from mybooking.core.models import AllowedUser
from telebot import types


def get_users(username: str) -> types.InlineKeyboardMarkup:
    users = AllowedUser.objects.all()
    markup = types.InlineKeyboardMarkup(row_width=2)
    print(users)
    for user in users:
        """ add in InlineKeyboard """
        if user.username == username:
            text = "На себя"
            callback_data = user.name
        else:
            text = user.name
            callback_data = user.name
        markup.add(
            types.InlineKeyboardButton(
                text=text, callback_data=callback_data
            )
        )
    return markup
