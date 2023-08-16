from django.conf import settings
from telegram import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from django.utils.translation import gettext as _

from main.models import Category


async def lang_button():
    buttons = []
    for lang in settings.LANGUAGES:
        buttons.append(InlineKeyboardButton(
            f'{lang[1]}', callback_data=f'{lang[0]}'
        ))

    return InlineKeyboardMarkup([buttons[i:i + 2] for i in range(0, len(buttons), 2)])


async def get_menu_key():
    button = [
        [KeyboardButton(_('Menu')), KeyboardButton(_('Sozlamalar'))],
        [KeyboardButton(_('🛒Korzina'))],
        [KeyboardButton(_('Biz bilan aloqa'))]
    ]
    return ReplyKeyboardMarkup(button, resize_keyboard=True)


async def category_button():
    button = []
    async for cat in Category.objects.filter(parent_id=11).all():
        button.append(
            InlineKeyboardButton(cat.name, callback_data=cat.id)
        )
    return InlineKeyboardMarkup([button[i:i + 2] for i in range(0, len(button), 2)])