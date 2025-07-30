import requests
import time
from pprint import pprint
from settings import TOKEN

send_message_url  = "https://api.telegram.org/bot8229527955:AAFNKPd82bE3ObqgMusWsN-bqV-7tjGnBzs/sendMessage"
update_message_url = "https://api.telegram.org/bot8229527955:AAFNKPd82bE3ObqgMusWsN-bqV-7tjGnBzs/getUpdates"

last_update_id = None
while True:
    
     # Agar oldingi update_id mavjud bo‘lsa, offset bilan yuboramiz
    params = {"offset": last_update_id + 1} if last_update_id else {}
    
    r = requests.get(update_message_url,params)
    
    if r.status_code == 200:
        data = r.json()
        result = data['result'] #list qabul qilib olyabman
        
        if result:   # malumot borligini tekshirib beradi
            message = result[-1]
            update_id = message['update_id']
            
            if last_update_id != update_id:
                text = message['message']['text']
                
                if text == "/start":
                    word = "Salom siz beckend dasturchilar botiga xush kelibsiz!"
                    params = {
                                "chat_id":message['message']['chat']['id'],
                                "text":word
                            }
                elif text == "/stop":
                    word = "xayr"
                    params = {
                                "chat_id":message['message']['chat']['id'],
                                "text":word
                            }
                    
                else:    
                    params = {
                                "chat_id":message['message']['chat']['id'],
                                "text":text
                            }
                
                requests.get(send_message_url,params)
                last_update_id = update_id
                time.sleep(2)
       
