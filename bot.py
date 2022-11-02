from telebot import TeleBot, types

from config import token
bot = TeleBot(token)


def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 #количетсво кнопок в строке
    btn1 = types.InlineKeyboardButton("Salam", callback_data="cb_yes")
    btn2 = types.InlineKeyboardButton("Menu", callback_data="menu")
    markup.add(btn1, btn2)
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "menu":
        show_menu(call.message)


def show_menu(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())

@bot.message_handler(commands=['start_a'])
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())



bot.infinity_polling()