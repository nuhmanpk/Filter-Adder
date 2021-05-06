import re
from typing import Optional

import telegram
from telegram import ParseMode, InlineKeyboardMarkup, Message, Chat
from telegram import Update, Bot, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot import dispatcher, LOGGER

@run_async
def filter(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    message = update.effective_message  # type: Optional[Message]
    message.reply_text("/filter Will not work for me \n use /add <filter name> {reply} For Adding new Filter ")

@run_async
def filters(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    message = update.effective_message  # type: Optional[Message]
    message.reply_text("Use /showfilters to Return all saved filters ")

@run_async
def donate(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    message = update.effective_message  # type: Optional[Message]
    message.reply_text("I Encourage your Mind for showing interest in donation, But I'm sorry we are working on a Secured Donation method. Please wait until it Go on production")

@run_async
def reply_keyboard_remove(bot: Bot, update: Update):
    reply_keyboard = []
    reply_keyboard.append([
        ReplyKeyboardRemove(
            remove_keyboard=True
        )
    ])
    reply_markup = ReplyKeyboardRemove(
        remove_keyboard=True
    )
    old_message = bot.send_message(
        chat_id=update.message.chat_id,
        text='Removing Connection Keyboard',
        reply_markup=reply_markup,
        reply_to_message_id=update.message.message_id
    )
    bot.delete_message(
        chat_id=update.message.chat_id,
        message_id=old_message.message_id
    )



__help__ = """
◆ Bot Name : *Filter Adder*
◆ Creator : [BUGHUNTER](http://t.me//bughunter0)
◆ Credits :  Myself
◆ Language : Python3
◆ Source Code :  [BUGHUNTERBOTS](https://t.me/bughunterbots)
◆ Server : Heroku
◆ Database : Postgre SQL
◆ Build Status : Stable(2.0)
◆ New feature : 2x Faster than version 1.9
"""
__mod_name__ = "About"


OLD_filterHANDLER = CommandHandler("filter",filter )
OLD_filtersHANDLER = CommandHandler("filters",filters )
DONATE_HANDLER = CommandHandler("donate",donate )
RMKEYBOARD_HANDLER = DisableAbleCommandHandler("rmkeyboard", reply_keyboard_remove)

dispatcher.add_handler(OLD_filterHANDLER)
dispatcher.add_handler(OLD_filtersHANDLER)
dispatcher.add_handler(DONATE_HANDLER)
dispatcher.add_handler(RMKEYBOARD_HANDLER)
