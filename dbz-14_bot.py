import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)
    
    try:
        username = msg['from']['username']
    except:
        firstname = msg['from']['first_name']
    user_id = msg['from']['id']
    
    
    
    if content_type == 'text':
        text = msg['text']
    
    if username == 'giusep92':
        bot.sendMessage(chat_id,'Rassegnati rimani STRANOSESSUALE qualsiasi cosa tu scriva!')
    else:
        bot.sendMessage(chat_id,text)
    
    
TOKEN = '756616900:AAHGeFWrGvONdLWHOYCXuiS2Sb1j_XgJ9YY'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ....')
# Keep the program running.
while 1:
    time.sleep(10)
