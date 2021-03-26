import requests

url = 'https://api.telegram.org/bot'
jsonData = {'chat_id': '-1001298945859',
            'text': 'MessageTest',
            'disable_notification': 'true'}
header = {"Content-Type": "application/json"}

#use the 'headers' parameter to set the HTTP headers:
response = requests.post(url, jsonData, headers=header)

print(response)
print(response.text)
