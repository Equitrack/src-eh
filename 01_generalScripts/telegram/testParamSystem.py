#!/bin/python3
import sys
import os.path
from os import path

numArgs = str(len(sys.argv))

if numArgs == "3":
    nameArgs = str(sys.argv[1])
    message = str(sys.argv[2])

def main():
    # validate correct num of params
    if numArgs == "3":

        # Select mode use
        if nameArgs == "-m" or nameArgs == "--message":
            sendMessage("message")

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
        sendMessage(option)
    else:
        print("The file: " + '"' + nameFile + '"' + " does not exists")

def sendMessage(option):
    # Check type data: message, load or read file.

    # . . . [ Continue ]
    print("option: " + option)

    if option == "read":
        # Read file
        text = open(nameArgs, "r")
        print(text.read())
    else:
        print("Error al leer el fichero")

main()
