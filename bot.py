import telebot

bot = telebot.TeleBot('6007795419:AAED467MOmJLZEV1KXDGbXzCOmD83RBHmr4')

from pytube import YouTube
from moviepy.editor import *


import validators

@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Здравствуйте, <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(content_types=["text"])
def text(message):
    valid = validators.url(message.text)
    if valid == True:
        try:
            link = message.text
            yt = YouTube(link)
            print("Url is valid")
            bot.send_message(message.chat.id, "Url is valid", parse_mode="html")
            stream = yt.streams.get_by_itag(18)
            s = stream.download()
            bot.send_message(message.chat.id, "Downloading the Video...", parse_mode="html")
            name = s + ".mp3"
            bot.send_message(message.chat.id, "Downloaded the Video", parse_mode="html")
            video = VideoFileClip(s)
            bot.send_message(message.chat.id, "Converting to mp3...", parse_mode="html")
            video.audio.write_audiofile(name)
            bot.send_message(message.chat.id, "Converted to mp3", parse_mode="html")
            # bot.send_message(message.chat.id, name)
            bot.send_audio(chat_id=message.chat.id, audio=open(name, 'rb'))
            bot.send_message(message.chat.id, "Done, enjoy", parse_mode="html")
        except:
            print("Url is invalid")
            bot.send_message(message.chat.id, "Url is invalid", parse_mode="html")

    else:
        print("Invalid url")
        bot.send_message(message.chat.id, "Invalid url", parse_mode="html")


bot.polling(none_stop=True)