# import requests
# from pprint import pprint
# from settings import TOKEN
# from printers import print_menu
# from Valyuta_replace.valyuta import valyuta_to_see

# update_message_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# send_message_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# last_update_id = None
# while True:
    
#     if isinstance(last_update_id,int):
#         update_params = {
#             "offset":last_update_id + 1
#         }
#     else:
#         update_params = {}
        
#     r = requests.get(update_message_url,params=update_params)

#     if r.status_code == 200:
#         result = r.json()['result']
        
#         if result :
#             message = result[-1]
             #last_update_id = message['update_id']
             
#             id = message['message']['from']['id']
#             text = message['message']['text']
            
#             if text == "/start":
#                 text = print_menu()
#                 send_params = {
#                     "chat_id":id,
#                     "text":text
#                 }
#             else:
#                 send_params = {
#                     "chat_id":id,
#                     "text":valyuta_to_see(text=text)
#                 }
#           
#             requests.get(send_message_url,params=send_params)

import requests
from settings import TOKEN
from printers import print_menu
from Valyuta_replace.valyuta import valyuta_to_see

update_message_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
send_message_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

last_update_id = None

while True:
    update_params = {"offset": last_update_id + 1} if isinstance(last_update_id, int) else {}

    r = requests.get(update_message_url, params=update_params)

    if r.status_code == 200:
        result = r.json().get("result", [])
        
        if result:
            message = result[-1]
            last_update_id = message["update_id"]  # har doim update_id yangilanadi

            if "message" in message:
                user_message = message["message"]
                chat_id = user_message["from"]["id"]
                text = user_message.get("text", "")

                # /start bo'lsa menyuni chiqaramiz
                if text == "/start":
                    reply_text = print_menu()
                else:
                    reply_text = valyuta_to_see(text)

                send_params = {
                    "chat_id": chat_id,
                    "text": reply_text,
                    "parse_mode": "Markdown"  # agar menyu markdown bo‘lsa
                }

                requests.get(send_message_url, params=send_params)

