from django.core.management.base import BaseCommand
from tgbot.application import app


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        app.run_polling()
