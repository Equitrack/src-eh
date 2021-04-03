#!/bin/python3

import os
import sys

if __name__ == "__main__":
    print(len(sys.argv))
    if(len(sys.argv) == 2):
        print("Dos argumentos")
    else:
        print("Diferente de dos argumentos")
        error_use();

def error_use():
    print("Used: " + sys.argv[0])

