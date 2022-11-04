from telebot import TeleBot, types
from pathlib import Path
from threading import *
import time
import pandas as pd
import random

from text_generator import rand_photo
from config import token
bot = TeleBot(token)

# a = {'id': [1], 'username': ['no_more_dopee'], 'pidor_count': [0]}
# df = pd.DataFrame(a)
# filepath = Path('data/pidor_db.json')
# df.to_json(filepath)

# c = pd.read_json('data/pidor_db.json')
# print(c)
#
# for i in range(len(c)):
#     print(c.column_1[i])

# print(c.column_1[0])
# print(len(c))
#
#


def gen_markup(): # фронт от Андрюхи
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 3 #количетсво кнопок в строке

    btn1 = types.InlineKeyboardButton("ПИДОР😡", callback_data="pidor")
    btn2 = types.InlineKeyboardButton("Регистрация😎", callback_data="reg")
    btn3 = types.InlineKeyboardButton("Таблица🤥", callback_data="table")
    btn4 = types.InlineKeyboardButton("Добавить в словарь", callback_data="dickt")

    markup.add(btn1)
    markup.add(btn2, btn3, btn4)

    return markup


def dict_start(chat_id):
    # rnd = random.randint(0,5)
    rnd = 0
    text_dict = {'text1':['Поиск пидорасика...'], 'text2': ['Проверка жоп у претендентов...'],
                 'text3':['Сегодня пидорас ']}
    df = pd.DataFrame(text_dict)
    filepath = Path(f'data/dict_data/dict_{chat_id}_db.json')
    df.to_json(filepath)


@bot.callback_query_handler(func=lambda call: True) # фронт от Андрюхи
def callback_query(call):
    if call.data == "pidor":
        pidor_menu(call.message)
    elif call.data == "table":
        table_menu(call.message)
    elif call.data == "reg":
        reg_menu(call.message)
    elif call.data == "dickt":
        dikt_menu(call.message)


def dikt_menu(message):
    bot.send_message(message.chat.id, "Словарь в разработке", parse_mode='html')

def reg_menu(message):                                       #вставить регистрацию
    bot.send_message(message.chat.id, "<u> /pidor_reg</u> 👈🏿 нажми для регистрации", parse_mode='html')


def pidor_menu(message):                                       #вставить регистрацию
    pidor(message.chat.id)


def table_menu(message):                                 #вставить таблицу
    pidor_stats(message)


@bot.message_handler(commands=['start_new_session'])
def start(message):
    bot.send_message(message.chat.id, f'<b>Hello <u>{message.from_user.username}</u></b>', parse_mode='html')
    a = {'id': [1], 'username': [message.from_user.username], 'pidor_count': [0]}
    df = pd.DataFrame(a)
    dict_start(message.chat.id)
    filepath = Path(f'data/pidor_{message.chat.id}_db.json')
    df.to_json(filepath)


@bot.message_handler(commands=['pidor_reg'])
def pidor_reg(message):
    temp_frame = pd.read_json(f'data/pidor_{message.chat.id}_db.json')
    temp_row = {'id': len(temp_frame)+1, 'username': message.from_user.username, 'pidor_count': 0}
    temp_frame = temp_frame.append(temp_row, ignore_index=True)
    if pd.Series(temp_frame["username"]).is_unique:
        filepath = Path(f'data/pidor_{message.chat.id}_db.json')
        temp_frame.to_json(filepath)
        print(temp_frame)
        bot.send_message(message.chat.id, f'<b>{message.from_user.username},'
                                          ' вы записаны в список пидорасов!</b>', parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'<b>{message.from_user.username},'
                                          ' вы уже давно стали гомосеком!</b>', parse_mode='html')


def pidor(id_chat):
    bot.send_message(id_chat, 'Поиск пидорасика...', parse_mode='html')
    time.sleep(3)
    bot.send_message(id_chat, 'Проверка жоп у претендентов...', parse_mode='html')
    time.sleep(3)
    temp_frame = pd.read_json(f'data/pidor_{id_chat}_db.json')
    rnd = random.randint(0, len(temp_frame)-1)
    gay = temp_frame.username[rnd]
    bot.send_message(id_chat, f'Пидорас найден!\n\nЭто <b><u>{gay}</u></b>!', parse_mode='html')
    temp_frame.at[rnd, 'pidor_count'] = temp_frame.pidor_count[rnd] + 1
    print(temp_frame)
    temp_frame.to_json(f'data/pidor_{id_chat}_db.json')


@bot.message_handler(commands=['pidor_stats'])
def pidor_stats(message):
    temp_frame = pd.read_json(f'data/pidor_{message.chat.id}_db.json')
    sort_frame = temp_frame.sort_values(by='pidor_count', ascending=False, kind="mergesort", ignore_index=True)
    print(sort_frame)
    a = '<b>Список пидорасов:</b>\n\n'
    for i in range(len(sort_frame)):
        a += f'<b>{i+1}. <u>{sort_frame.username[i]}</u></b> (x{sort_frame.pidor_count[i]}).\n\n'
    bot.send_message(message.chat.id, a, parse_mode='html')


@bot.message_handler(commands=['start_a']) # фронт от Андрюхи
def message_handler(message):
    photo = rand_photo()
    text = "А какой сегодня пидор ты?🥵"
    bot.send_photo(message.chat.id, photo=photo, caption=text, reply_markup=gen_markup())


# def timer():
#     while True:
#         print('a')
#         time.sleep(1)


if __name__ == '__main__':
    # t1 = Thread(target=timer)
    # print('ochko')
    bot.infinity_polling()
    # print('jopa')
    # t1.start()
    # t2.start()