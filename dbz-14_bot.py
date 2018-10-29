import telepot, time, sqlite3
from telepot.loop import MessageLoop
from pprint import pprint

conn = sqlite3.connect('dbz-14.db')
c = conn.cursor()
c.execute('''CREATE TABLE comandi
             (comando text, descrizione text)''')
c.execute("INSERT INTO comandi VALUES ('/aiuto','Conoscere i comandi disponibili e quanto riguarda il BOT')")
c.execute("INSERT INTO comandi VALUES ('/riassunto','Riassunto avventura')")
c.execute("INSERT INTO comandi VALUES ('/personaggi','Personaggi partecipanti')")
c.execute("INSERT INTO comandi VALUES ('/luoghivisitati','I luoghi del mondo fantastico')")
conn.commit()
conn.close()


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
    elif text == '/aiuto':
        bot.sendMessage(chat_id,'Le funzioni disponibili sono /riassunto, /personaggi, /luoghivisitati')
    elif text == '/riassunto':
        bot.sendMessage(chat_id,'Dopo innumerevoli peripezie e aver messo alla prova il loro allineamento massacrando dei poveracci in un carcere, i nostri eroi sono entrati nel posto segreto, hanno ucciso delle mummie e risolto un indovinello e sono pronti ora alla battaglia finale')
    elif text == '/personaggi':
        bot.sendMessage(chat_id,'Ancora da implementare. Comunque sono tutti froci')
    elif text == '/luoghivisitati':
        bot.sendMessage(chat_id,'Ancora da implementare. Comunque sono tutti brutti e noiosi')
    else:
        bot.sendMessage(chat_id,text)
    
    
TOKEN = '756616900:AAHGeFWrGvONdLWHOYCXuiS2Sb1j_XgJ9YY'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ....')
# Keep the program running.
while 1:
    time.sleep(10)
