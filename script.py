from pytube import YouTube
from moviepy.editor import *


#path = 'C:\Music\\'

#video_url = input("Please enter the video URL: ")
#yt = YouTube(video_url)


#stream = yt.streams.get_by_itag(18)
#s = stream.download()
#name = s + ".mp3"

#video = VideoFileClip(s)
#video.audio.write_audiofile(name)

def conv(link, Youtube=None):
    yt = Youtube(link)
    stream = yt.streams.get_by_itag(18)
    s = stream.download()
    name = s + ".mp3"

    video = VideoFileClip(s)
    mp3 = video.audio.write_audiofile(name)
    return mp3


@bot.message_handler()
def get_link(user_input):
    yt = YouTube(user_input)
    stream = yt.streams.get_by_itag(18)
    s = stream.download()
    name = s + ".mp3"

    video = VideoFileClip(s)
    mp3 = video.audio.write_audiofile(name)
    bot.send_message(user_input.chat.id, mp3)
