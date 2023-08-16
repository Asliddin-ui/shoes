from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from django.utils.translation import gettext as _


async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(_('Settings tanlandi'))


handlers = [
    MessageHandler(filters.ALL, settings)
]