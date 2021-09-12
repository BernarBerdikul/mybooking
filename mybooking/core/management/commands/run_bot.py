import logging
from django.core.management.base import BaseCommand
from ...telegram_bot import bot


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Run telegram bot."

    def handle(self, *args, **options):
        """ run telegram bot """
        bot.polling(skip_pending=True)
