#!/bin/bash

# execute with root user

pathFile=`readlink -f $(which python3)`

if [ -f "$pathFile" ]; then
   echo "existe";
else
   echo "Python3 no existe"
fi

#setcap cap_setuid+ep /usr/bin/$binary
#echo "Status capability: $(getcap /usr/bin/$binary)"

