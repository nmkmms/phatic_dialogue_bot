import chatbot
import telebot

TOKEN = "YOUR_TOKEN_HERE"

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    answear = chatbot.chat(message.text)
    bot.reply_to(message, answear)

bot.polling()
