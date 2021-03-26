#!/usr/bin/python3

import requests

token = "1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c"
url = "https://api.telegram.org/bot" + token + "/getUpdates"

response = requests.get(url)

# Muestra los headers de respuesta
for i in response.headers:
    print(i + ":" + response.headers[i])

print(response.status_code)

