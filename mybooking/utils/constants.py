###############################################################################
""" PROJECT CONSTANTS """
OBJECTS_PER_PAGE_IN_ADMIN = 100  # pagination in admin page

DAYS_OF_THE_WEEK = ("ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС")

START_WORK_TIME = "8:00"
END_WORK_TIME = "21:00"
###############################################################################
""" TELEGRAM BOT """
ERROR_CHAT_ID = 421591563
ROOM_INFO = "Посмотреть бронь"
###############################################################################
""" CORE APP """

USER = "USER"
SUPER_ADMIN = "SUPER_ADMIN"

USER_TYPES = (
    (USER, "Пользователь"),
    (SUPER_ADMIN, "Супер админ"),
)
