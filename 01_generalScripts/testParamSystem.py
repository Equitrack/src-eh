#!/bin/python3
import sys

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

def checkFile(nameFile):
    print("Check if exist: " + nameFile)

# validate correct num of params
if nArgs == "3":

    nameArgs = str(sys.argv[1])

    # Select mode use

    if nameArgs == "-m" or nameArgs == "--message":
        print("Send message")

    elif nameArgs == "-l" or nameArgs == "--load":
        checkFile(str(sys.argv[2]))
        print("Send file")

    elif nameArgs == "-r" or nameArgs == "--read":
        checkFile(str(sys.argv[2]))
        print("Read File")

    else:
        useError()
else:
    useError()
