#!/bin/bash

# ver procesos en tiempo real
#ps -eo command

# DIFF
# Es una herramienta para comparar cadenas de texto y encontrar las diferencias

oldProcess=$(ps -eo command)

while true; do
   newProcess=$(ps -eo command)
   diff <(echo "$oldProcess") <(echo "$newProcess") | grep "[\>\<]" | grep -v "kworker"
   oldProcess=$newProcess
done
