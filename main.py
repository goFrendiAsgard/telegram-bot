import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler

# https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/conversationbot.py

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def add(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text # /add 4 5
    cmd, n1, n2 = user_message.split(" ")
    result = float(n1) + float(n2)
    update.message.reply_text(f'{n1} + {n2} = {result}')

def mean(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text # /mean 4 5 6 7 8
    parameters = user_message.split(" ") # ['/mean', '4', '5', '6', '7', '8']
    n_list = parameters[1:] # ['4', '5', '6', '7', '8']
    total = 0
    for n in n_list:
        total = total + float(n)
    result = total/len(n_list)
    update.message.reply_text(f'average of {n_list} = {result}')


updater = Updater(os.getenv('TELEGRAM_TOKEN'))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('add', add))
updater.dispatcher.add_handler(CommandHandler('mean', mean))


updater.start_polling()
updater.idle()
