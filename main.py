import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler

# https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/conversationbot.py

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater(os.getenv('TELEGRAM_TOKEN'))

updater.dispatcher.add_handler(CommandHandler('hello', hello))


updater.start_polling()
updater.idle()