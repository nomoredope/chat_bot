from telebot import TeleBot, types
import random
import time

from config import token
bot = TeleBot(token)


def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 #количетсво кнопок в строке
    btn1 = types.InlineKeyboardButton("ПИДОР", callback_data="cb_yes")
    btn2 = types.InlineKeyboardButton("Регистрация", callback_data="reg")
    btn3 = types.InlineKeyboardButton("Таблица", callback_data="table")
    markup.add(btn1)
    markup.add(btn2, btn3)
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "reg":
        table(call.message)
    elif call.data == "table":
        reg(call.message)


def reg(message):                                       #вставить регистрацию
    bot.send_message(message.chat.id, "Yes/no?")
def table(message):                                 #вставить таблицу
    bot.send_message(message.chat.id, "Yes/no?")


def rand_photo():
    rnd=random.randint(0,5)
    photo = 'https://i.pinimg.com/736x/c5/3b/8e/c53b8efc3ebc0fa6df3455bddeb3a5d2.jpg'
    if rnd == 0:
        photo = 'https://i.pinimg.com/564x/2b/47/8f/2b478f068c6ee2295cb11aef8685d625.jpg'
    elif rnd == 1:
        photo = 'https://i.pinimg.com/564x/48/ab/e0/48abe0c33d6c95f886816738219a5f32.jpg'
    elif rnd == 2:
        photo = 'https://i.pinimg.com/564x/d5/d8/1d/d5d81d89f61ce7d4238ded3dd733281a.jpg'
    elif rnd == 3:
        photo = 'https://i.pinimg.com/564x/94/f7/ad/94f7ad1598831a379164c0c519d2f87f.jpg'
    elif rnd == 4:
        photo = 'https://i.pinimg.com/564x/38/bc/97/38bc9726373f611bd21b66dde7dbe290.jpg'
    elif rnd == 5:
        photo = 'https://i.pinimg.com/564x/3a/4c/09/3a4c096c72d7466b557becc5ecb81f07.jpg'
    return photo


@bot.message_handler(commands=['start_a'])
def message_handler(message):
    photo = rand_photo()
    text = "А какой сегодня пидор ты?"
    #bot.send_message(message.chat.id, text=text, reply_markup=gen_markup())
    bot.send_photo(message.chat.id, photo=photo, caption=text, reply_markup=gen_markup())


bot.infinity_polling()