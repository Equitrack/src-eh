#!/bin/python3

import requests

token = 

url = "https://api.telegram.org/bot" + token + "/sendDocument"

chat_id ='-595788453' 

data = {'chat_id': chat_id,
        'document' : '/home/tony/Documents/mastermind/src-eh/01_generalScripts/telegram/document.txt',
        'disable_notification': 'true'}

header = {"Content-Type": "application/json"}

response = requests.post(url, data, header)

if response.status_code == 200:
    print(response.text)
else:
    print("Response text: " + str(response.status_code))

