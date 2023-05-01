import telebot

bot = telebot.TeleBot('6007795419:AAED467MOmJLZEV1KXDGbXzCOmD83RBHmr4')


import os
import validators

@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Здравствуйте, <b>{message.from_user.first_name}    {message.from_user.last_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(content_types=["text"])
def text(message):
    valid = validators.url(message.text)
    if valid == True:
        try:
            yt_dlp_audio = os.system("yt-dlp -f 140 " + str(message))
        except:
            bot.send_message(message.chat.id, "Error", parse_mode="html")

    else:
        bot.send_message(message.chat.id, "Url is invalid", parse_mode="html")

bot.polling(none_stop=True)