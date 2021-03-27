#!/bin/python3
import sys

# verificar que haya parámetros
print("Número de parámetros: "+ str(len(sys.argv)))

nArgs = str(len(sys.argv))

def useError():
    print("Use:")
    print("./testParamSystem.py <option> <file/text>")
    print("Options:")
    print("\t-m\tSend message")
    print("\t-f\tRead file and send message")
    print('Examples:')
    print('\t./testParamSystem.py -m "Low disk space"')
    print('\t./testParamSystem.py -f logs.txt')

if nArgs == "4":
    print("Uso correcto")
else:
    useError()
