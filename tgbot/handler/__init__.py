from .start import handlers as start_handler
from .handler_for_keyboards import handlers as handler_keyboard
from .settings import handlers as setting_handler
from .catalog import handlers as catalog_handler


handlers = start_handler + catalog_handler + setting_handler + handler_keyboard
