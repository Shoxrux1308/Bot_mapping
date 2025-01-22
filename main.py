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
    query.answer()  
    if query.data == "smartphones":
        keyboard = [
            [InlineKeyboardButton("Samsung", callback_data='samsung')],
            [InlineKeyboardButton("Apple", callback_data='apple')],
            [InlineKeyboardButton("Xiaomi", callback_data='xiaomi')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your brand:", reply_markup=reply_markup)
    elif query.data == "laptops":
        keyboard = [
            [InlineKeyboardButton("HP", callback_data='hp')],
            [InlineKeyboardButton("Lenovo", callback_data='lenovo')],
            [InlineKeyboardButton("Asus", callback_data='asus')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your brand:", reply_markup=reply_markup)
    elif query.data == "tv":
        keyboard = [
            [InlineKeyboardButton("Samsung", callback_data='samsung_tv')],
            [InlineKeyboardButton("LG", callback_data='lg_tv')],
            [InlineKeyboardButton("Toshiba", callback_data='toshiba_tv')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your brand:", reply_markup=reply_markup)
    elif query.data == "cameras":
        keyboard = [
            [InlineKeyboardButton("Canon", callback_data='canon_camera')],
            [InlineKeyboardButton("Nikon", callback_data='nikon_camera')],
            [InlineKeyboardButton("Sony", callback_data='sony_camera')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your brand:", reply_markup=reply_markup)
    elif query.data == "mens_clothing":
        keyboard = [
            [InlineKeyboardButton("Sweatshirts", callback_data='sweatshirts')],
            [InlineKeyboardButton("Jeans", callback_data='jeans')],
            [InlineKeyboardButton("T-Shirts", callback_data='t_shirts')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "womens_clothing":
        keyboard = [
            [InlineKeyboardButton("Dresses", callback_data='dresses')],
            [InlineKeyboardButton("Skirts", callback_data='skirts')],
            [InlineKeyboardButton("Jackets", callback_data='jackets')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "kids_clothing":
        keyboard = [
            [InlineKeyboardButton("Baby Girls Clothing", callback_data='baby_girls_clothing')],
            [InlineKeyboardButton("Baby Boys Clothing", callback_data='baby_boys_clothing')],
            [InlineKeyboardButton("Kids Clothing", callback_data='kids_clothing_product')]  # Changed callback data
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "beds":
        keyboard = [
            [InlineKeyboardButton("Single Beds", callback_data='single_beds')],
            [InlineKeyboardButton("Double Beds", callback_data='double_beds')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "tables":
        keyboard = [
            [InlineKeyboardButton("Coffee Tables", callback_data='coffee_tables')],
            [InlineKeyboardButton("Dining Tables", callback_data='dining_tables')],
            [InlineKeyboardButton("Kitchen Tables", callback_data='kitchen_tables')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "chairs":
        keyboard = [
            [InlineKeyboardButton("Wooden Chairs", callback_data='wooden_chairs')],
            [InlineKeyboardButton("Arm Chairs", callback_data='arm_chairs')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "sofas":
        keyboard = [
            [InlineKeyboardButton("Sofas", callback_data='sofas')],
            [InlineKeyboardButton("Armchairs", callback_data='armchairs')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your product:", reply_markup=reply_markup)
    elif query.data == "fiction":
        keyboard = [
            [InlineKeyboardButton("Harry Potter", callback_data='harry_potter')],
            [InlineKeyboardButton("The Lord of the Rings", callback_data='lord_of_the_rings')],
            [InlineKeyboardButton("The Hunger Games", callback_data='hunger_games')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your book:", reply_markup=reply_markup)
    elif query.data == "non_fiction":
        keyboard = [
            [InlineKeyboardButton("The Alchemist", callback_data='alchemist')],
            [InlineKeyboardButton("To Kill a Mockingbird", callback_data='to_kill_a_mockingbird')],
            [InlineKeyboardButton("Pride and Prejudice", callback_data='pride_and_prejudice')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Choose your book:", reply_markup=reply_markup)

updater = Updater(TOKEN, use_context=True)  
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text & ~Filters.command, message_handler)  
button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(button_handler)
updater.start_polling()
updater.idle()