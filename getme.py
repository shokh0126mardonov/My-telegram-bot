import requests
from settings import TOKEN

url = f"https://api.telegram.org/bot{TOKEN}/getMe"
r = requests.get(url=url)

print(r.url)