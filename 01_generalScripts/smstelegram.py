#!/usr/bin/python3
import requests
import json
import os

url = 'https://api.telegram.org/bot' + "1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c" + "/sendMessage"
mensaje= 'mensaje desde una variable'

jsonData = {'chat_id': '-595788453',
            'text': mensaje,
            'disable_notification': 'true'}

header = {"Content-Type": "application/json"}

#use the 'headers' parameter to set the HTTP headers:
response = requests.post(url, jsonData, header)

# Muestra los headers de respuesta
for i in response.headers:
    print(i + ": " + response.headers[i])

print("\n")

if response.status_code == 200:
    f = open("response.json", "w")
    f.write(response.text)
    f.close()
   
    # Pretty Printing JSON string back
    print(json.dumps(json.loads(response.text), indent = 4, sort_keys=True))

else:
    print("status code: " + str(response.status_code))

