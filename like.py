import os
from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater,MessageHandler,CallbackContext,Filters,CommandHandler
TOKEN=os.environ.get("TOKEN")

def start(update:Update,context:CallbackContext):
    keyboard = [
        ["🛍 Electronics"],
        ["🛍 Clothing"],  
        ["🛍 Furniture"],
        ["🛍 Books"]
    ]
    replay_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text("Hi! Welcome to the Bot_mapping. Please select the category you want to like.",reply_markup=replay_markup)
def message_handler(update:Update,context:CallbackContext):
    if update.message.text == "🛍 Electronics":
        keyboard=[
                [InlineKeyboardButton("👎",callback_data="dislike"),InlineKeyboardButton("👍",callback_data="like")]
        ]
        reply_markup=InlineKeyboardMarkup(keyboard)
        update.message.reply_photo(photo="https://minapi.beemarket.uz/prod-media/productImages/thumbnails/medium/1726834437OHIFEMxr0Z6k.webp",reply_markup=reply_markup)
    elif update.message.text == "🛍 Clothing":
        keyboard=[
                [InlineKeyboardButton("👎",callback_data="dislike"),InlineKeyboardButton("👍",callback_data="like")]
                ]
        reply_markup=InlineKeyboardMarkup(keyboard)
        update.message.reply_photo(photo="https://img.kwcdn.com/thumbnail/s/a7226cc31860a1f81679797785b513ec_7841334e6b57.jpg?imageView2/2/w/800/q/70/format/webp",reply_markup=reply_markup)
    elif update.message.text == "🛍 Furniture":
        keyboard=[
                [InlineKeyboardButton("👎",callback_data="dislike"),InlineKeyboardButton("👍",callback_data="like")]
                ]
        reply_markup=InlineKeyboardMarkup(keyboard)
        update.message.reply_photo(photo="https://cb.scene7.com/is/image/Crate/cb_mSC_20241101_Furniture_TVStandsStorage?bfc=on&wid=500&qlt=80&op_sharpen=1",reply_markup=reply_markup)
    elif update.message.text == "🛍 Books":
        keyboard=[
            [InlineKeyboardButton("👎",callback_data="dislike"),InlineKeyboardButton("👍",callback_data="like")]
        ]
        reply_markup=InlineKeyboardMarkup(keyboard)
        update.message.reply_photo(photo="https://images.theconversation.com/files/45159/original/rptgtpxd-1396254731.jpg?ixlib=rb-4.1.0&q=45&auto=format&w=754&fit=clip",reply_markup=reply_markup)
update=Updater(TOKEN)
dispatcher=update.dispatcher
dispatcher.add_handler(CommandHandler("start",start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
update.start_polling()
update.idle()
