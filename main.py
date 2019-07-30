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
    bot.send_chat_action(message.chat.id, 'typing')
    if message.text.lower == 'что делаешь, лео?':
        bot.send_message(message.chat.id, 'Привет! Я учусь читать и писать', reply_to_message_id=message.message_id)


bot.polling(True)