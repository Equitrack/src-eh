#!/bin/python3

import os
import sys
import requests
import re

def error_use():
    print("Used: " + sys.argv[0] + " <url> " + "<words> \n")
    print("\tExample:")
    print("\t" + sys.argv[0] + " https://supermex.com.mx " + '"2060, 2070, 2080"')

if __name__ == "__main__":
    if(len(sys.argv) == 3):
        response = requests.get(sys.argv[1])
        if response.status_code == 200:
            print("Executing ...")
            keys = str(sys.argv[2])
            
        else:
            print("Error: Status code [" + response.status_code + "]")
    else:
        error_use()




