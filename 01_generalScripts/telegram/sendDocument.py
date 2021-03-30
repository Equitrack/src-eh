#!/bin/python3

import requests

token = "1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c"

url = "https://api.telegram.org/bot" + token + "/sendDocument"

chat_id ='-595788453'

path = str("/home/tony/Documents/mastermind/src-eh/01_generalScripts/telegram/document.txt")

data = {'chat_id': chat_id,
        'document' : path }

header = {"Content-Type": "application/json"}

response = requests.post(url, data, header)

if response.status_code == 200:
    print(response.text)
else:
    print("Response status: " + str(response.status_code))

