#!/bin/bash

echo `python3 --version | sed 's/  *//g' | cut -d '.' -f 1,2`
setcap cap_setuid(0)+ep /usr/bin/$(python3 --version | sed 's/  *//g' | cut -d '.' -f 1,2)

