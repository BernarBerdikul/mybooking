import telebot
import os
from mybooking.core.bot_services.create_booking_object_db import \
    create_booking_object_db, update_booking_object
from mybooking.core.bot_services.get_days import get_days
from mybooking.core.bot_services.get_room_info import get_room_with_schedule
from mybooking.core.bot_services.get_rooms import get_rooms
from mybooking.core.bot_services.get_users import get_users
from mybooking.core.bot_services.is_user_allowed import is_user_allowed
from mybooking.utils import constants
from mybooking.utils.validators import time_format_validation

TOKEN = os.getenv("telegram_bot_token")
API_KEY = os.getenv("telegram_bot_address")

# create a new Telegram Bot
bot = telebot.TeleBot("1918534669:AAEEDi-rJubL4Ogy1QNNqejU2knRUo0BRxE")


# command description used in the "help" command
commands = {
    'start': 'Начать работу с ботом',
    'help': 'Информация о доступных командах',
    'rooms': 'Возвращает список кабинетов',
}


@bot.message_handler(commands=['help'])
def command_help(message):
    """ generate help text out of the commands
        dictionary defined at the top """
    chat_id = message.chat.id
    help_text = "Доступные команды: \n"
    for key in commands:
        help_text += f"/{key}: {commands[key]}\n"
    bot.send_message(chat_id=chat_id, text=help_text)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    from mybooking.core.bot_services.get_rooms import get_rooms
    chat_id = message.from_user.id
    user_instance = message.from_user
    if is_user_allowed(username=user_instance.username):
        rooms = get_rooms()
        bot.send_message(
            chat_id=chat_id, text="Выберите комнату", reply_markup=rooms)
    else:
        bot.send_message(
            chat_id=chat_id, text="К сожалению у вас нет доступа")


@bot.message_handler(commands=["rooms"])
def send_rooms(message):
    chat_id = message.from_user.id
    rooms = get_rooms()
    bot.send_message(
        chat_id=chat_id, text="Выберите комнату", reply_markup=rooms
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith('№'))
def callback_query(call):
    chat_id = call.from_user.id
    room_name = call.data
    bot.delete_message(chat_id=chat_id, message_id=call.message.id)
    days = get_days(room_name=room_name)
    bot.send_message(
        chat_id=chat_id, text="Выберите дату", reply_markup=days
    )


@bot.callback_query_handler(
    func=lambda call: call.data.startswith(constants.ROOM_INFO)
)
def callback_query(call):
    chat_id = call.from_user.id
    room = get_room_with_schedule(room_name=call.data.split()[-1])
    if room.bookings.count() == 0:
        text = "Брони нет"
    else:
        text = "Расписание на неделю"
    bot.answer_callback_query(call.id, text=text)
    for booking in room.bookings.order_by('day'):
        if booking.user is not None:
            weekday = f"\n{constants.DAYS_OF_THE_WEEK[booking.day.weekday()]}: {booking.day}:"
            text += f"{weekday}\n\t\t\t\t\t с {booking.start_time} - по {booking.end_time} " \
                    f"Занял: {booking.user.name}"
    bot.send_message(
        chat_id=chat_id, text=text
    )


@bot.callback_query_handler(
    func=lambda call: call.data.split()[0] in constants.DAYS_OF_THE_WEEK
)
def callback_query(call):
    booking_date = call.data.split()[-1]
    room_name = call.data.split()[-3]
    chat_id = call.from_user.id
    bot.delete_message(chat_id=chat_id, message_id=call.message.id)
    bot.answer_callback_query(call.id, text="Введите время начала в формате {время в часах}:{время в минутах}")
    bot.send_message(
        chat_id=chat_id,
        text='Введите время начала в формате {время в часах}:{время в минутах}'
    )
    bot.register_next_step_handler(
        call.message, input_start_time, booking_date, room_name
    )


def input_start_time(message, booking_date, room_name, success=True):
    try:
        chat_id = message.chat.id
        start_time = message.text
        if success is False:
            bot.send_message(
                chat_id=chat_id, text='Не верный формат времени, попробуйте еще раз'
            )
        if time_format_validation(value=start_time):
            bot.send_message(
                chat_id=chat_id,
                text='Введите время конца в формате {время в часах}:{время в минутах}?'
            )
            bot.register_next_step_handler(
                message, input_end_time, start_time, booking_date, room_name)
        else:
            bot.register_next_step_handler(
                message, input_start_time, booking_date, room_name, success=False
            )
    except Exception as e:
        bot.reply_to(message, 'Упс, попробуйте начать по новой /start')


def input_end_time(message, start_time, booking_date, room_name, success=True):
    try:
        chat_id = message.chat.id
        end_time = message.text
        if success is False:
            bot.send_message(
                chat_id=chat_id, text='Не верный формат времени, попробуйте еще раз'
            )
        if time_format_validation(end_time) and end_time > start_time:
            new_booking_object = create_booking_object_db(
                start_time=start_time,
                end_time=end_time,
                booking_date=booking_date,
                room_name=room_name
            )
            users = get_users(
                username=message.from_user.username,
                new_booking_object_id=new_booking_object.id
            )
            bot.send_message(
                chat_id=chat_id,
                text='На кого арендуете?', reply_markup=users
            )
        else:
            bot.register_next_step_handler(
                message, input_end_time, start_time, booking_date, room_name, success=False
            )
    except Exception as e:
        bot.reply_to(message, 'Упс, попробуйте начать по новой /start')


@bot.callback_query_handler(
    func=lambda call: call.data.startswith("-@")
)
def callback_query(call):
    chat_id = call.from_user.id
    booking_id = call.data.split()[-1]
    user_id = call.data.split()[-3]
    update_booking_object(
        booking_id=booking_id, user_id=user_id
    )
    bot.send_message(
        chat_id=chat_id, text='Вы успешно забронировали'
    )


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if not message.text.startswith(('/', '№', '-')):
        bot.send_message(
            chat_id=message.from_user.id,
            text="Я создан для отправки бронирования кабинетов, "
                 "а не для того что бы разговаривать с вами 😐",
        )
