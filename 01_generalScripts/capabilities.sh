#!/bin/bash

# execute with root user

pathFile=`which python3`

if [ -d "$path" ]; then
   echo "existe";
else
   echo "Python3 no existe"
fi

#setcap cap_setuid+ep /usr/bin/$binary
#echo "Status capability: $(getcap /usr/bin/$binary)"

