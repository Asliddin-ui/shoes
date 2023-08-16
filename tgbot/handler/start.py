from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler

from tgbot.customhandler import CustomHandler
from tgbot.keyboards import get_key, lang_button
from tgbot.models import TelegramUser
from django.utils.translation import gettext as _, activate


async def user_load(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    try:
        tg_user = await TelegramUser.objects.aget(telegram_user_id=user_id)
        await hello(update, context, True)
    except TelegramUser.DoesNotExist:
        tg_user = await TelegramUser.objects.acreate(
            update.effective_user.username,
            update.effective_user.first_name,
            update.effective_user.last_name
        )

    context.tguser = tg_user

    activate(tg_user.language)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE, edit=False) -> None:
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

    if edit:
        try:
            print("A")
            await update.effective_message.edit_text(**params2)
        except:
            print('B')
            # await update.effective_message.delete()
            await update.effective_message.reply_text(**params2)
    else:
        print('C')
        await update.effective_message.reply_text(**params)


async def change_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user: TelegramUser = context.tguser
    user.language = context.match.group(1)
    await user.asave()
    activate(user.language)

    await update.callback_query.answer(_('Til o`zgartirildi'))
    await hello(update, context, True)


handlers = [
    (CustomHandler(user_load), 0),
    CommandHandler('start', hello),
    CallbackQueryHandler(change_language, pattern="^(uz|ru|en)$"),
]
