import telebot
import functions
import time, os


token = os.environ.get('TOKEN', None)
bot = telebot.TeleBot(token)


def typing_action(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)


@bot.message_handler(commands=['start'])
def handle_command(message):
    typing_action(message)
    bot.send_message(message.chat.id, 'Привет! Меня зовут Леопольд и я помогу '
                                      'разобраться тебя в терминологии IT')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() == 'что делаешь, лео?':
        typing_action(message)
        bot.send_message(message.chat.id, 'Привет! Я учусь читать и писать', reply_to_message_id=message.message_id)
    else:
        functions.update()
        message_list = message.text.split()
        words = functions.word_and_synonims
        discriptions = functions.words_discription
        answer = ''
        for word in message_list:
            for i in range(len(words)):
                if word in words[i]:
                    answer = word + ' или же ' + words[i][0] + ' - это ' + discriptions[i]
        bot.send_message(message.chat.id, answer, reply_to_message_id=message.message_id)


bot.polling(True)