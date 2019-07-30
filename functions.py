def read_text(text):
    for i in text:
        if i in dictionary:
            bot.send_message(message.chat.id, answer)