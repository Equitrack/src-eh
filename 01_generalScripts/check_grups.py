import requests

token = "1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c"
url = "https://api.telegram.org/bot" + token + "/getUpdates"

response = requests.get(url)

print(response.headers)
print(response.text)
