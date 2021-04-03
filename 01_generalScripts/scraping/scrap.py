#!/bin/python3

import os
import sys

def error_use():
    print("Used: " + sys.argv[0])

if __name__ == "__main__":
    print(len(sys.argv))
    if(len(sys.argv) == 2):
        print("Continue..."
    else:
        error_use();


