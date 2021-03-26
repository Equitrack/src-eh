import requests

url = 'https://api.telegram.org/bot'
myobj = {'chat_id': '-1001298945859',
        ''

#use the 'headers' parameter to set the HTTP headers:
x = requests.post(url, data = myobj, headers = {"HTTP_HOST": "MyVeryOwnHost"})

print(x.text)
