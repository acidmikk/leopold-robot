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
    bot.send_message(message.chat.id, 'Привет!✋🏻 Я — Бот Леопольд. Хочу помогать тебе разобраться '
                                      'с профессиональным сленгом ИТ-специалистов.\n\n'
                                      'Буду жить в этом чате и раскрывать истинные '
                                      'значения непонятных слов! ☺')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    functions.update()
    message_list = message.text.split()
    words = functions.word_and_synonims
    discriptions = functions.words_discription
    main_word = functions.real_name
    answer = ''
    for word in message_list:
        for i in range(len(words)):
            if word.lower() in words[i]:
                answer += word + ' '
                if word != words[i][0] or word != main_word[i]:
                    answer += 'или же ' + main_word[i] + ' '
                answer += '- это ' + discriptions[i] + '\n'
    bot.send_message(message.chat.id, answer[:-1], reply_to_message_id=message.message_id)


bot.polling(True)