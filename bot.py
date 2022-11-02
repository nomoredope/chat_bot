from telebot import TeleBot, types

from config import token
bot = TeleBot(token)


@bot.message_handler(commands=['start_a'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("👋🏿 Салам потный", url='https://i.pinimg.com/564x/2b/47/8f/2b478f068c6ee2295cb11aef8685d625.jpg')
    btn2 = types.InlineKeyboardButton("😎 Меню", url="https://i.pinimg.com/564x/2b/47/8f/2b478f068c6ee2295cb11aef8685d625.jpg")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'<b>Hello <u>{message.from_user.username}</u></b>', parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['menu_a'])
def menu(message):
    bot.send_message(message.chat.id, f'<b><u>Меню</u></b>', parse_mode='html')

bot.infinity_polling()