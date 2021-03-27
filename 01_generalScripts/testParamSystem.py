#!/bin/python3
import sys

# verificar que haya parámetros
print("Número de parámetros: "+ str(len(sys.argv)))

nArgs = str(len(sys.argv))

def useError():
    print("Use:")
    print("./testParamSystem.py <option> <file/text>")
    print("Options:")
    print("\t-m, --message\tSend message")
    print("\t-l, --load\tSend file")
    print("\t-r, --read\tRead file and send message")
    print('Examples:')
    print('\t./testParamSystem.py -m "Low disk space"')
    print('\t./testParamSystem.py --loadFile logs.txt')

if nArgs == "3":
    print("Uso correcto")
    nameArgs = str(sys.argv[1])
    print("Nombre del argumento: " + nameArgs)
    if nameArgs == "-m" or nameArgs == "--message":
        print("Send message")
    elif nameArgs == "-l" or nameArgs == "--load":
        print("Send file")
    elif nameArgs == "-r" or nameArgs == "--read":
        print("Read File")
    else:
        useError()
else:
    useError()
