import telebot
from chat_gpt import chat_gpt

API_TOKEN = '<your_telegram_bot_api_token>'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """Hi there, I am EchoBot.\nI am here to echo your kind words back to you. Just say anything nice and I'll reply""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    res_ai = chat_gpt(message.text)
    bot.reply_to(message, res_ai)


bot.infinity_polling()
