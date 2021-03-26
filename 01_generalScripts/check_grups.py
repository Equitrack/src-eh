#!/usr/bin/python3

import requests
import json

token = "1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c"

url = "https://api.telegram.org/bot" + token + "/getUpdates"

response = requests.get(url)

# Muestra los headers de respuesta
for i in response.headers:
    print(i + ": " + response.headers[i])

if response.status_code == 200:
    f = open("response.json", "w")
    f.write(response.text)
    f.close()
    
    for j in json.loads(response.text).keys():
        print(j + ": " + str(json.loads(response.text).keys()[j]))

else:
    print("Status code: " + response.status_code)

