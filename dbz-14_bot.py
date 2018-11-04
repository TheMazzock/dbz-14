import telepot, time, sqlite3, random, csv
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from pprint import pprint

conn = sqlite3.connect('dbz-14.db')
conn.isolation_level = None
c = conn.cursor()
buffer = ""
start_keyboard = [["Personaggi","Luoghi"],["Riassunto",
                  "Dadi"],
                  ["Aiuto"]]
start_markup = ReplyKeyboardMarkup(keyboard=start_keyboard, one_time_keyboard=False)
dadi_keyboard = [["1d4"],["2d4"],["3d4"],["1d6"],["2d6"],["3d6"],["1d8"],["2d8"],["3d8"],["1d10"],["2d10"],["3d10"],["1d12"],["2d12"],["1d20"],["1d100"],["Esci"]]
dadi_markup = ReplyKeyboardMarkup(keyboard=dadi_keyboard, one_time_keyboard=False)
listadeidadi = ["1d4","2d4","3d4","1d6","2d6","3d6","1d8","2d8","3d8","1d10","2d10","3d10","1d12","2d12","1d20","1d100"]

"""
with open('personaggi.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|')
    for row in spamreader:
        print
"""

"""
def database(text):
    while True:
    line = text
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print(cur.fetchall())
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""
 """

def lancia_dado(x):
    return random.randint(1,x)

def dadi(x):
    if len(x) == 3:
        numero = int(x[0])
        dado = int(x[2])
    elif len(x) == 4:
        numero = int(x[0])
        dado = int(x[2:4])
    elif len(x) == 5:
        numero = int(x[0])
        dado = int(x[2:5])
    print(dado)
    risultato = 0
    testo_risultato = ""
    for i in range(numero):
        ris=lancia_dado(dado)
        testo_risultato += str(ris)
        testo_risultato += " "
        risultato += ris
    testo_risultato += "totale: "
    testo_risultato += str(risultato)
    return testo_risultato
    
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
    
    if text == '/start':
        bot.sendMessage(chat_id, str("Dimmi avventuriero, cazzo vuoi?"), reply_markup=start_markup)
    elif text == 'Aiuto':
        bot.sendMessage(chat_id,'Le funzioni disponibili sono /riassunto, /personaggi, /luoghivisitati, /database (Questa lasciatela stare)')
    elif text == 'Riassunto':
        bot.sendMessage(chat_id,'Dopo innumerevoli peripezie e aver messo alla prova il loro allineamento massacrando dei poveracci in un carcere, i nostri eroi sono entrati nel posto segreto, hanno ucciso delle mummie e risolto un indovinello e sono pronti ora alla battaglia finale')
    elif text == 'Personaggi':
        bot.sendMessage(chat_id,'Ancora da implementare. Comunque sono tutti froci')
    elif text == 'Luoghi':
        bot.sendMessage(chat_id,'Ancora da implementare. Comunque sono tutti brutti e noiosi')
    elif text == '/database':
        bot.sendMessage(chat_id,'Ancora da implementare. Non la toccate che vi mozzo le dita')
    elif text in listadeidadi:
        lanciodadi = dadi(text)
        bot.sendMessage(chat_id, lanciodadi)
    elif text == 'Dadi':
        bot.sendMessage(chat_id, str("Che dado vuoi lanciare?"), reply_markup=dadi_markup)
    elif text == 'Esci':
        bot.sendMessage(chat_id, str("Dimmi avventuriero, cazzo vuoi?"), reply_markup=start_markup)
        
    else:
        bot.sendMessage(chat_id,text)
    
    
TOKEN = '756616900:AAHGeFWrGvONdLWHOYCXuiS2Sb1j_XgJ9YY'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ....')
# Keep the program running.
while 1:
    time.sleep(10)
conn.close()
