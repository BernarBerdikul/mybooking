import json
import os
from django.views import View
from django.http import JsonResponse
from telebot import types
import telebot


TOKEN = os.getenv("telegram_bot_token")
BOT_URL = os.getenv("telegram_bot_address")
bot = telebot.TeleBot(TOKEN)


def process_telegram_event(update_json):
    update = types.Update.de_json(update_json, bot)
    bot.process_new_updates([update])


def index(request):
    return JsonResponse({"error": "sup hacker"})


class TelegramBotWebhookView(View):
    # WARNING: if fail - Telegram webhook will be delivered again. 
    # Can be fixed with async celery task execution
    def post(self, request, *args, **kwargs):
        process_telegram_event(json.loads(request.body))

        # TODO: there is a great trick to send data in webhook response
        # e.g. remove buttons
        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request processed. But nothing done"})
