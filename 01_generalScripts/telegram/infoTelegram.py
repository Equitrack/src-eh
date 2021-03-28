#!/usr/bin/python3

import requests
import json

token = "1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c"

url = "https://api.telegram.org/bot" + token + "/getUpdates"

response = requests.get(url)

# Muestra los headers de respuesta
print("[*****Headers*****]")
for i in response.headers:
    print(i + ": " + response.headers[i])

if response.status_code == 200:
    f = open("response.json", "w")
    f.write(response.text)
    f.close()
    
    # Pretty Printing JSON string back
    print(json.dumps(json.loads(response.text), indent = 4, sort_keys=True))
        

else:
    print("Status code: " + response.status_code)

