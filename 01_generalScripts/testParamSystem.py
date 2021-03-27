#!/bin/python3
import sys

# verificar que haya parámetros
print("Número de parámetros: "+ str(len(sys.argv)))

nParams = str(len(sys.argv))

if nParams == "3":
    print("Use:")
    print("./testParamSystem.py <option> <file/text>")
    print("Options:")
    print("\t-m\tSend message")
    print("\t-f\tRead file and send message")
    print('Examples:')
    print('\t./testParamSystem.py -m "Low disk space"')
    print('\t./testParamSystem.py -f logs.txt')

