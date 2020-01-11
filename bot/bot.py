#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from telegram import ParseMode, InlineKeyboardMarkup, \
    InlineKeyboardButton
from telegram.ext import InlineQueryHandler, ChosenInlineResultHandler, \
    CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

from shared_vars import updater, dispatcher
from start_bot import start_bot

def mamalo(bot, update, args, job_queue):
    """Handler for the /start command"""
    chat = update.message.chat
    bot.sendMessage(chat.id,text="Mamalo {args}".format(args = args[0]))

# Add all handlers to the dispatcher and run the bot
dispatcher.add_handler(CommandHandler('mamalo', mamalo, pass_args=True, pass_job_queue=True))

start_bot(updater)
updater.idle()
