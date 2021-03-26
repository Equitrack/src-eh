#!/bin/python3
import sys

# verificar que haya parámetros
if str(len(sys.argv)) == "1":
    print("Uso: ./testParamSystem.py <option> <file/text>")
    print("Options:")
    print("\t-m\tSend message")
    print("\t-f\tRead file and send message")

# print("Parámetro n: " + str(sys.argv[1]))
