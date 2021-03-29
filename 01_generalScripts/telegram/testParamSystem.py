#!/bin/python3
import requests
import sys
import os.path
from os import path


# C H A N G E _ T H I S _ V A L U E _ T O K E N

token="1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c" 

numArgs = str(len(sys.argv))

if numArgs == "3":
    nameArgs = str(sys.argv[1])
    message = str(sys.argv[2])

def main():
    # validate correct num of params
    if numArgs == "3":

        # Select mode use
        if nameArgs == "-m" or nameArgs == "--message":
            sendMessage(message)

        elif nameArgs == "-l" or nameArgs == "--load":
            checkFile(message, "load")

        elif nameArgs == "-r" or nameArgs == "--read":
            checkFile(message, "read")

        else:
            useError()
    else:
        useError()

    
def useError():
    print("Usage: ./testParamSystem.py <option> <file/text>")
    print("Options:")
    print("\t-m, --message\tSend message")
    print("\t-l, --load\tSend file")
    print("\t-r, --read\tRead file and send message")
    print('Examples:')
    print('\t./testParamSystem.py -m "Low disk space"')
    print('\t./testParamSystem.py --loadFile logs.txt')

def checkFile(nameFile, option):
    if path.exists(nameFile) == True:
        if option == "read": 
            text = open(message, "r")
            sendMessage(text.read())
        elif option == "load":

            print("Cargando el fichero")
            sendFile(nameFile)
        else:
            print("The file: " + '"' + nameFile + '"' + " does not exists")

def sendMessage(textPlain):
    url = 'https://api.telegram.org/bot' + token + "/sendMessage"
    chat_id ='-595788453',
    data = {'chat_id' : chat_id,
            'text' : textPlain,
            'disable_notification': 'true'}
    header = {"Content-Type": "application/json"}

    response = requests.post(url, data, header)

    # View headers
    print("[*****Headers*****]")
    for i in response.headers:
        print(i + ": " + response.headers[i])
    
    print("[\n*****Contenido*****]")
    if response.status_code == 200:
        print(response.text)
    else:
        print("Status code: " + str((response.status_code)))

main()
