#!/usr/bin/python3

import requests
import os.path
from os import path

token = "1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c"

url = "https://api.telegram.org/bot" + token + "/getUpdates"

response = requests.get(url)

# Muestra los headers de respuesta
for i in response.headers:
    print(i + ": " + response.headers[i])

if response.status_code == 200:
    print("\n[***Response:***]\n")
    print( response.text + "\n")
else:
    print("Status code: " + response.status_code)

