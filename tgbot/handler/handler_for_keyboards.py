from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from django.utils.translation import gettext as _
from tgbot.handler.settings import settings


async def keyboard_handlers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    if msg == _('Sozlamalar'):
        await settings(update, context)
    elif msg == _('🛒Korzina'):
        await update.effective_message.reply_text('Korzina tanlandi')


handlers = [
    MessageHandler(filters.ALL, keyboard_handlers)
]
