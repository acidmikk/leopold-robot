import telebot
import os
import functions
import time


token = os.environ.get('TOKEN', None)
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.send_message(message.chat.id, 'Привет! Меня зовут Леопольд и я помогу '
                                      'разобраться тебя в терминологии IT')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Я учусь читать')


bot.polling(True)