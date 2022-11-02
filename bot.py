from telebot import TeleBot
from pathlib import Path
import pandas as pd
import time
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


@bot.message_handler(commands=['start_m'])
def start(message):
    bot.send_message(message.chat.id, f'<b>Hello <u>{message.from_user.username}</u></b>', parse_mode='html')


@bot.message_handler(commands=['pidor_reg'])
def pidor_reg(message):
    bot.send_message(message.chat.id, f'<b>{message.from_user.username},'
                                      ' вы записаны в список пидорасов!</b>', parse_mode='html')
    temp_frame = pd.read_json('data/pidor_db.json')
    temp_row = {'id': len(temp_frame)+1, 'username': message.from_user.username, 'pidor_count': 0}
    temp_frame = temp_frame.append(temp_row, ignore_index=True)
    filepath = Path('data/pidor_db.json')
    temp_frame.to_json(filepath)
    print(temp_frame)


@bot.message_handler(commands=['pidor'])
def pidor(message):
    bot.send_message(message.chat.id, 'Поиск пидорасика...', parse_mode='html')
    time.sleep(3)
    bot.send_message(message.chat.id, 'Проверка жоп у претендентов...', parse_mode='html')
    time.sleep(3)
    temp_frame = pd.read_json('data/pidor_db.json')
    rnd = random.randint(0, len(temp_frame)-1)
    gay = temp_frame.username[rnd]
    bot.send_message(message.chat.id, f'Пидорас найден!\n\n Это {gay}')
    temp_frame.at[rnd, 'pidor_count'] = temp_frame.pidor_count[rnd] + 1
    print(temp_frame)


bot.infinity_polling()
