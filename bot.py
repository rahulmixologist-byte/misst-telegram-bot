import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

AUTO_MESSAGE = """
1️⃣ Feet content  
2️⃣ I am Misstress  
3️⃣ Submissive will allow to contact me  

✳️ Paid Session available  
❇️ Demo charge 77/- 1 minute  

✅ Chat session 99/- 8 minutes  
✅ Voice call 199/- 5 minutes  
✅ Video call 470/- 10 minutes  

✳️ Offer price for video call session  
✅ 199/- 5 minutes  

✳️ Feet pic sell 70/- two pics  
✳️ Feet video sell 200/- 1 minute  

🛑 Non paid slave not allowed  
❌ No real meet
"""

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    with open("photo.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=AUTO_MESSAGE)

bot.polling(non_stop=True)
