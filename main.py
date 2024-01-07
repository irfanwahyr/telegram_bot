import os

import telebot
from pytube import YouTube

from alive import alive

TOKEN = os.environ['API_TOKEN']
bot = telebot.TeleBot(TOKEN)

alive()

@bot.message_handler(commands=['start'])
def start(messege):
  bot.send_message(messege.chat.id,
     '''WERRBOT\n
     Halo, selamat menggunakan WerrBot.\n
     BOT ini adalah Buatan Bang iwer.\n
     Jika ingin meminta bantuan BOT tekan\n
     /help
     '''
  )


@bot.message_handler(commands=['help'])
def help(messege):
  bot.send_message(messege.chat.id,
     '''BANTUAN COMMANDS PADA BOT\n
     - /start - Memulai BOT\n
     - /help - meminta bantuan\n
     - /download_YT - download Video Youtube\n
     '''
  )

@bot.message_handler(commands=['download_YT'])
def download_YT(message):
    bot.send_message(message.chat.id,'Silahkan Paste Link Video Youtube!!!')

# Menangani pesan yang berisi link YouTube
@bot.message_handler(func=lambda _: True)
def handle_message(message):
    if message.text.startswith('http'):
        try:
            # Mengunduh video dari link yang diberikan
            yt = YouTube(message.text)
            video = yt.streams.get_highest_resolution()

            # Menyimpan video ke dalam file
            if video:
              video.download()
              # Mengirimkan video kepada pengguna
              with open(video.title + ".mp4", 'rb') as video_file:
                bot.send_video(message.chat.id, video_file, caption=video.title)
              # hapus file
              os.remove(video.title + ".mp4")
                
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id,
                'Terjadi kesalahan saat mengunduh video. Pastikan Link Benar')
    else:
        bot.send_message(message.chat.id, "Mohon berikan link YouTube yang valid.")

bot.polling()
