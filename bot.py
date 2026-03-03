import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello 👋 I am Misst Assistant Bot (Free Version)")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Commands:\n/start - Start bot\n/help - Help menu")

@bot.message_handler(func=lambda message: True)
def reply(message):
    text = message.text.lower()

    if "hi" in text:
        bot.reply_to(message, "Hello Rahul 👋 How can I help you?")
    elif "name" in text:
        bot.reply_to(message, "My name is Misst Assistant 🤖")
    elif "menu" in text:
        bot.reply_to(message, "Available commands:\n/start\n/help")
    else:
        bot.reply_to(message, "I am a free version bot 😊")

bot.polling()
