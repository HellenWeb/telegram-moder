# Import

from aiogram import Bot, Dispatcher
from config import token
import logging
from sqlighter import SQLighter
from filter import IsAdminFilter

# Logging

logging.basicConfig(level=logging.INFO)

# Default Variebles

bot = Bot(token)
dp = Dispatcher(bot)
db = SQLighter("db.db")

"""Filter"""

dp.filters_factory.bind(IsAdminFilter)
