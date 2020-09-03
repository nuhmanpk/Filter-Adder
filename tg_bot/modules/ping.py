

import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import is_user_admin, user_admin
from tg_bot.modules.helper_funcs.extraction import extract_user


EDIT_SLEEP = 3
EDIT_TIMES = 8

pingpong = [
            "Checking Webhooks....",
            "Webhook found ! ",
            "Checking Server Uplink..",
            "Loading... 20.63%\n[███░░░░░░░░░░░]",    
            "Loading... 50.21%\n[███████░░░░░]",
            "Loading... 93.50%\n[███████████░░░]",
            "Loading....  100%\n[███████████████]",
]

@user_admin
@run_async
def ping(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('Checking server status') 
    for x in range(EDIT_TIMES):
        msg.edit_text(pingpong[x%5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("Hey, I'm Up")

PING_HANDLER = DisableAbleCommandHandler("ping", ping)
dispatcher.add_handler(PING_HANDLER)
__mod_name__ = "SOURCE CODE"
__handlers__ = [PING_HANDLER]
