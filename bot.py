from telebot import TeleBot, types
from pathlib import Path
from threading import *
import time
import pandas as pd
import random

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


def rand_photo(): # фронт от Андрюхи
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


def gen_markup(): # фронт от Андрюхи
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 #количетсво кнопок в строке
    btn1 = types.InlineKeyboardButton("ПИДОР", callback_data="pidor")
    btn2 = types.InlineKeyboardButton("Регистрация", callback_data="reg")
    btn3 = types.InlineKeyboardButton("Таблица", callback_data="table")
    markup.add(btn1)
    markup.add(btn2, btn3)
    return markup


@bot.callback_query_handler(func=lambda call: True) # фронт от Андрюхи
def callback_query(call):
    if call.data == "pidor":
        pidor_menu(call.message)
    elif call.data == "table":
        table_menu(call.message)
    elif call.data == "reg":
        reg_menu(call.message)


def reg_menu(message):                                       #вставить регистрацию
    bot.send_message(message.chat.id, "<u>Для регистрации: /pidor_reg</u>", parse_mode='html')


def pidor_menu(message):                                       #вставить регистрацию
    pidor(message.chat.id)


def table_menu(message):                                 #вставить таблицу
    pidor_stats(message)


@bot.message_handler(commands=['start_new_session'])
def start(message):
    bot.send_message(message.chat.id, f'<b>Hello <u>{message.from_user.username}</u></b>', parse_mode='html')
    a = {'id': [1], 'username': [message.from_user.username], 'pidor_count': [0]}
    df = pd.DataFrame(a)
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
    text = "А какой сегодня пидор ты?"
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
