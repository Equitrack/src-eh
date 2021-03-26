#!/bin/python3
import sys

# verificar que haya parámetros
if str(len(sys.argv)) == "1":
    print("Use:")
    print("./testParamSystem.py <option> <file/text>")
    print("Options:")
    print("\t-m\tSend message")
    print("\t-f\tRead file and send message")
    print('Examples:')
    print('\t./testParamSystem.py -m "Low disk space"')
    print('\t./testParamSystem.py -f logs.txt')

elif str(len(sys.argv)) == "3":
    print(str(sys.argv[1]))

else
    print("else")
