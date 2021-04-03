#!/bin/python3

import os
import sys
import requests

def error_use():
    print("Used: " + sys.argv[0] + " <url> " + "<words>")
    print("\tExample:\n")
    print(sys.argv[0] + " https://supermex.com.mx {2060, 2070, 2080}")

if __name__ == "__main__":
    print(len(sys.argv))
    if(len(sys.argv) == 3):
        response = requests.get(sys.argv[1])
        if response.status_code == 200:
            print("Executing ...")
        else:
            print("Error: Status code [" + response.status_code + "]")
    else:
        error_use()




