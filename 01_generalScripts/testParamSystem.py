#!/bin/python3
import sys

# verificar que haya parámetros
if str(len(sys.argv)) == "1":
    print("\tUso: ./testParamSystem.py <option> <file/text>")
    print("\tOptions:")
    print("\t\t-m\tSend message")
    print("\t\t-f\tRead file and send message")

# print("Parámetro n: " + str(sys.argv[1]))
