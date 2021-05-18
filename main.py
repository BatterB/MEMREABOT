import telebot
from telebot import types
import requests
import lyricsgenius
import json

genius = lyricsgenius.Genius('1QNGIpXDI4sa74sNMrgfDZQ0WPVmKO8R4NPJiJLGxiN04bvjSH1JVb4P_bEoKV1U')

bot = telebot.TeleBot('1511345495:AAFOvoTaNaiXFVAR6qLRY7bSE1zu2mzowsY')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Введите имя исполнителя')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    artist_name = message.text.lower()
    global artist
    artist = genius.search_artist(artist_name, max_songs=0, sort="title")
    msg = bot.send_message(message.from_user.id, 'Введите название песни')
    bot.register_next_step_handler(msg, menu)

def menu (message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Топ песен")
    if message == 'Топ песен':
        msg = bot.send_message(message.from_user.id, 'Введите необходимое количество песен')
        bot.register_next_step_handler(msg, get_lyrics_song)
    elif message == 'Альбомы':
        msg = bot.send_message(message.from_user.id, 'Введите название песни')
        bot.register_next_step_handler(msg, get_lyrics_song)
    elif message == 'Текст песни':
        msg = bot.send_message(message.from_user.id, 'Введите название песни')
        bot.register_next_step_handler(msg, get_lyrics_song)


def get_lyrics_song(message):
    song_name = message.text.lower()
    song = artist.song(song_name)
    bot.send_message(message.from_user.id, song.lyrics)


bot.polling(none_stop=True)

