#!/bin/python3

from telnetlib import Telnet
import re

flag = ""

with Telnet('pong.threatsims.com', 2346) as tn:
    i=1
    while(i<100):
        line = tn.read_until(b"\n").decode("utf-8").replace('\n','')
        if(line != ""):
            print(line)
            if(len(line) == 1):
                flag = flag + line         
                tn.write(bytes(line + "\n", 'utf-8'))
        i=i+1

print("[*] Result: \n", flag)
