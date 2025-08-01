import requests
url = "https://api.telegram.org/bot8229527955:AAFNKPd82bE3ObqgMusWsN-bqV-7tjGnBzs/sendMessage"


params = {
    "chat_id":7088856987,
    "text":"salom"
}

requests.get(url=url,params=params)