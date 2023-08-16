from django.db import models


class TelegramUser(models.Model):
    telegram_user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255, default=None, blank=True, null=True)
    first_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    language = models.CharField(max_length=2, default='uz')
