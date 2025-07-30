import requests
from pprint import pprint
from settings import TOKEN

url = "https://api.telegram.org/bot8229527955:AAFNKPd82bE3ObqgMusWsN-bqV-7tjGnBzs/sendMessage"

params = {
    "chat_id":7088856987,
    "text":"Salom Bekend dasturchilari botiga xush kelibsiz"
}

requests.get(url,params)





















# import requests
# from pprint import pprint
# from settings import TOKEN

# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# params = {
#     "chat_id":7088856987,
#     "text":"Salom hammaga"
# }

# r = requests.get(url=url,params=params)
# print(r.status_code)