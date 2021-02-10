import telebot
bot = telebot.TeleBot('1511345495:AAFOvoTaNaiXFVAR6qLRY7bSE1zu2mzowsY')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'гнида обращайся ко мне, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'хуйло проснись':
        bot.send_message(message.from_user.id, 'Пошел нахуй')
    else:
        bot.send_message(message.from_user.id, 'повторил тварь')

bot.polling(none_stop=True)
