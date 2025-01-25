import os
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

TOKEN = os.environ.get('TOKEN') 

def start(update, context):
    keyboard = [
        ["🛍 Electronics"],
        ["🛍 Clothing"],  
        ["🛍 Furniture"],
        ["🛍 Books"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("Welcome to our store! Choose an option:", reply_markup=reply_markup)

updater = Updater(TOKEN)  
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)                                   
updater.start_polling()
updater.idle()