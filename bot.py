import telebot
from database import Database


bot = telebot.TeleBot("6966475696:AAFSKj66T4ciD6jGz8Rk1krbdI_AM7fPdFE")

stack = {}
db = Database()

@bot.message_handler(commands=['start'])
def start(ms):
    bot.send_message(ms.chat.id, "Welcome")
    fn = ms.from_user.first_name
    n = db.add_users(fn, ms.from_user.username, ms.from_user.id)
    bot.reply_to(ms,n)
    
    stack[ms.chat.id] = "kutish"
    
@bot.message_handler(func=lambda x: True)
def response(ms):
    chat_id = ms.chat.id
    
    if chat_id in stack and stack[chat_id] == "kutish":
        bot.send_message(chat_id, ms.text)

def main():
    bot.polling()

if __name__ == '__main__':
    main()
