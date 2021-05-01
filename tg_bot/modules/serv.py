import re
from typing import Optional

import telegram
from telegram import ParseMode, InlineKeyboardMarkup, Message, Chat
from telegram import Update, Bot
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown

from tg_bot import dispatcher, LOGGER

@run_async
def old_filter(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    message = update.effective_message  # type: Optional[Message]
    message.reply_text("Error")



__help__ = """
◆ Bot Name : *Filter Adder*
◆ Creator : [BUGHUNTER](http://t.me//bughunter0)
◆ Credits :  Myself
◆ Language : Python3
◆ Source Code :  [BUGHUNTERBOTS](https://t.me/bughunterbots)
◆ Server : Heroku
◆ Database : Postgre SQL
◆ Build Status : Stable(1.9)
◆ New feature : Remote connection Option Added
"""
__mod_name__ = "About"


OLD_HANDLER = CommandHandler("filter",old_filter )

dispatcher.add_handler(OLD_HANDLER)
