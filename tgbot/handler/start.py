from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler

from tgbot.customhandler import CustomHandler
from tgbot.keyboards import get_key, lang_button
from tgbot.models import TelegramUser
from django.utils.translation import gettext as _, activate


async def user_load(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_user, _ = await TelegramUser.objects.aget_or_create(defaults={
        "username": update.effective_user.username,
        "first_name": update.effective_user.first_name,
        "last_name": update.effective_user.last_name,
        "language": update.effective_user.language_code,
    }, telegram_user_id=update.effective_user.id)

    context.user_data['edit'] = _
    context.user_data['tg_user'] = tg_user
    context.edit = True
    activate(tg_user.language)
    context.user_data['lang'] = False


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    params = {
        'text': _('Xush kelibsiz {}. Botdan foydalanish uchun tilni tanlang: ').format(
            update.effective_user.first_name),
        'reply_markup': await lang_button()
    }
    params2 = {
        'text': _('Quyidagi menulardan birini tanlang ').format(
            update.effective_user.first_name),
        'reply_markup': await get_key()
    }

    if not context.user_data['edit'] and not context.user_data['lang']:
        await update.effective_message.reply_text(**params2)
    elif context.user_data['lang'] and not context.user_data['edit']:
        await update.effective_message.delete()
        await update.effective_message.reply_text(**params2)
    else:
        await update.effective_message.reply_text(**params)


async def change_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user: TelegramUser = context.user_data['tg_user']
    user.language = context.match.group(1)
    await user.asave()
    activate(user.language)

    await update.callback_query.answer(_('Til o`zgartirildi'))
    context.user_data['lang'] = True
    await hello(update, context)


handlers = [
    (CustomHandler(user_load), 0),
    CommandHandler('start', hello),
    CallbackQueryHandler(change_language, pattern="^(uz|ru|en)$"),
]
