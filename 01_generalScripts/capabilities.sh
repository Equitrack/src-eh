#!/bin/bash

# execute with root user

pathFile=`readlink -f $(which python3)`

if [ -f "$pathFile" ]; then
   whoami

else
   echo "Python3 no existe"
fi

#echo "Status capability: $(getcap /usr/bin/$binary)"

