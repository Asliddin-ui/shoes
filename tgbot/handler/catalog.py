from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from django.utils.translation import gettext as _

from tgbot.handler.handler_for_keyboards import keyboard_handlers
from tgbot.keyboards import cat_button


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == _('Menu'):
        await update.effective_message.reply_text(_('Kerakli maxsulot bo`limini tanlang'),
                                              reply_markup=await cat_button())
    else:
        await keyboard_handlers(update, context)


handlers = [
    MessageHandler(filters.ALL, menu)
]
