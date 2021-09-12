import logging
import os
from django.core.management.base import BaseCommand
from ...telegram_bot import bot


logger = logging.getLogger(__name__)


TOKEN = os.getenv("telegram_bot_token")
BOT_URL = "https://mybooking-bot.herokuapp.com/"


class Command(BaseCommand):
    help = "Run telegram bot."

    def handle(self, *args, **options):
        """ run telegram bot """
        bot.remove_webhook()
        bot.set_webhook(url=f"{BOT_URL}{TOKEN}")
        bot.polling(skip_pending=True)
