from googletrans import Translator
from telebot import TeleBot
tarjimon=Translator()

bot=TeleBot('5710693992:AAGpdIv31BAEoSBtr8fqPqf5iRKXWww6gIQ')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu aleykum Tarjimon botiga hush kelibsiz!"
    javob+="\nMatn kiriting: "
    bot.reply_to(message,javob)

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    msg=message.text
    til=tarjimon.detect(msg).lang
    if til=='en':
        javob=(tarjimon.translate(msg,dest='uz')).text
        bot.reply_to(message,javob)
    else:
        javob=(tarjimon.translate(msg,dest='en')).text
        bot.reply_to(message,javob)

bot.polling()



