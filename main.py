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
def message_handler(update, context):
    if update.message.text == "🛍 Electronics":
        keyboard = [
            [InlineKeyboardButton("Smartphones", callback_data='smartphones')],
            [InlineKeyboardButton("Laptops", callback_data='laptops')],
            [InlineKeyboardButton("TV", callback_data='tv')],
            [InlineKeyboardButton("Cameras", callback_data='cameras')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Choose your product:", reply_markup=reply_markup)
    elif update.message.text == "🛍 Clothing":  # Ensure no trailing space here
        keyboard = [
            [InlineKeyboardButton("Men's Clothing", callback_data='mens_clothing')],
            [InlineKeyboardButton("Women's Clothing", callback_data='womens_clothing')],
            [InlineKeyboardButton("Kids Clothing", callback_data='kids_clothing')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Choose your product:", reply_markup=reply_markup)
    elif update.message.text == "🛍 Furniture":
        keyboard = [
            [InlineKeyboardButton("Beds", callback_data='beds')],
            [InlineKeyboardButton("Tables", callback_data='tables')],
            [InlineKeyboardButton("Chairs", callback_data='chairs')],
            [InlineKeyboardButton("Sofas", callback_data='sofas')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Choose your product:", reply_markup=reply_markup)
    elif update.message.text == "🛍 Books":
        keyboard = [
            [InlineKeyboardButton("Fiction", callback_data='fiction')],
            [InlineKeyboardButton("Non-Fiction", callback_data='non_fiction')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Choose your product:", reply_markup=reply_markup)
def button(update, context):
    query = update.callback_query 

    if query.data == "smartphones":
        keyboard = [
            [InlineKeyboardButton("Samsung", url="https://t.me/texnomart")],
            [InlineKeyboardButton("Apple", url="https://t.me/texnomart")],
            [InlineKeyboardButton("Xiaomi", url="https://t.me/texnomart")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your brand:", reply_markup=reply_markup)
    elif query.data == "laptops":
        keyboard = [
            [InlineKeyboardButton("HP", url="https://t.me/texnomart")],
            [InlineKeyboardButton("Lenovo", url="https://t.me/texnomart")],
            [InlineKeyboardButton("Asus", url="https://t.me/texnomart")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your brand:", reply_markup=reply_markup)
    elif query.data == "tv":
        keyboard = [
            [InlineKeyboardButton("Samsung",url="https://t.me/texnomart")],
            [InlineKeyboardButton("LG", url="https://t.me/texnomart")],
            [InlineKeyboardButton("Toshiba", url="https://t.me/texnomart")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your brand:", reply_markup=reply_markup)
    elif query.data == "cameras":
        keyboard = [
            [InlineKeyboardButton("Canon", url="https://t.me/chinasamarqand")],
            [InlineKeyboardButton("Nikon", url="https://t.me/chinasamarqand")],
            [InlineKeyboardButton("Sony", url="https://t.me/chinasamarqand")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your brand:", reply_markup=reply_markup)
    elif query.data == "mens_clothing":
        keyboard = [
            [InlineKeyboardButton("Sweatshirts", url="https://t.me/chinasamarqand")],
            [InlineKeyboardButton("Jeans", url="https://t.me/chinasamarqand")],
            [InlineKeyboardButton("T-Shirts", url="https://t.me/chinasamarqand")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "womens_clothing":
        keyboard = [
            [InlineKeyboardButton("Dresses", url="https://t.me/chinasamarqand")],
            [InlineKeyboardButton("Tops", url="https://t.me/chinasamarqand")],
            [InlineKeyboardButton("Skirts", url="https://t.me/chinasamarqand")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "kids_clothing":
        keyboard = [
            [InlineKeyboardButton("Baby Girls Clothing", url="https://t.me/sam_online_kids_shop")],
            [InlineKeyboardButton("Baby Boys Clothing", url="https://t.me/sam_online_kids_shop")],
            [InlineKeyboardButton("Kids Clothing", url="https://t.me/sam_online_kids_shop")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "beds":
        keyboard = [
            [InlineKeyboardButton("Single Beds", url="https://t.me/samarkandmebllarolami")],
            [InlineKeyboardButton("Double Beds", url="https://t.me/samarkandmebllarolami")],
            [InlineKeyboardButton("King Beds", url="https://t.me/samarkandmebllarolami")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)        
    elif query.data == "tables":
        keyboard = [
            [InlineKeyboardButton("Sofas", url="https://t.me/samarkandmebllarolami")],
            [InlineKeyboardButton("Chairs", url="https://t.me/samarkandmebllarolami")],
            [InlineKeyboardButton("Armchairs", url="https://t.me/samarkandmebllarolami")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "chairs":
        keyboard = [
            [InlineKeyboardButton("Leather Chairs", url="https://t.me/samarkandmebllarolami")],
            [InlineKeyboardButton("Wooden Chairs", url="https://t.me/samarkandmebllarolami")],            
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)        
    elif query.data == "sofas":
        keyboard = [
            [InlineKeyboardButton("Sofas", url="https://t.me/elektron_kutubxona_8")],
            [InlineKeyboardButton("Loveseats", url="https://t.me/elektron_kutubxona_8")],
            [InlineKeyboardButton("Couches", url="https://t.me/elektron_kutubxona_8")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "fiction":
        keyboard = [
            [InlineKeyboardButton("Harry Potter", url="https://t.me/elektron_kutubxona_8")],
            [InlineKeyboardButton("The Lord of the Rings", url="https://t.me/elektron_kutubxona_8")],
            [InlineKeyboardButton("The Hunger Games", url="https://t.me/elektron_kutubxona_8")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your book:", reply_markup=reply_markup)
    elif query.data == "non_fiction":
        keyboard = [
            [InlineKeyboardButton("The Great Gatsby", url="https://t.me/elektron_kutubxona_8")],
            [InlineKeyboardButton("To Kill a Mockingbird", url="https://t.me/elektron_kutubxona_8")],
            [InlineKeyboardButton("Pride and Prejudice", url="https://t.me/elektron_kutubxona_8")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your book:", reply_markup=reply_markup) 

updater = Updater(TOKEN)  
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text & ~Filters.command, message_handler) 
button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(button_handler)                                   
updater.start_polling()
updater.idle()