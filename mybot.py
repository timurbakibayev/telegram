import telepot
import time
import urllib3
from logic import question

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"

bot = telepot.Bot('549769681:AAHL_1uwvmBIbGuLyaNTDJYiVVJ3PGn1YFc')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, question(msg["text"], chat_id))

bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
