#!/usr/bin/python3

import requests

token = "1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c"
url = "https://api.telegram.org/bot" + token + "/getUpdates"

response = requests.get(url)

jsonHeaders = response.headers
content = response.text

print(jsonHeaders)
print("status code: " + response.status_code)

for i in jsonHeaders:
    print(i + ":" + jsonHeaders[i])

