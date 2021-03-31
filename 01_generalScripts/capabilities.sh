#!/bin/bash

binary=`python3 --version | sed 's/  *//g' | cut -d '.' -f 1,2`
setcap cap_setuid+ep /usr/bin/$binary

