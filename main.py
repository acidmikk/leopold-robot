import telebot
import os


token = os.environ.get('TOKEN', None)
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def handle_command(message):
    bot.send_message(message.chat.id, 'привет!')


bot.polling(True)