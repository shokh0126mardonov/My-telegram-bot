import requests
from pprint import pprint
from settings import TOKEN

url = f"https://api.telegram.org/bot{TOKEN}/getMe"
result = requests.get(url)
print(result.url)



























# import requests
# from pprint import pprint
# from settings import TOKEN

# url = f"https://api.telegram.org/bot{TOKEN}/getMe"

# r = requests.get(url)
# print(r.url)
