import telebot
import requests

req = requests.get("http://webservices.mirea.ru/upload/iblock/f81/%D0%98%D0%98%D0%A2_1%D0%BA_20-21_%D0%B2%D0%B5%D1%81%D0%BD%D0%B0.xlsx")

bot = telebot.TeleBot('1511345495:AAFOvoTaNaiXFVAR6qLRY7bSE1zu2mzowsY')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Какого уебана могут назвать, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'хуйло проснись':
        bot.send_message(message.from_user.id, 'Пошел нахуй')
    else:
        bot.send_message(message.from_user.id, 'повторил тварь')

bot.polling(none_stop=True)
