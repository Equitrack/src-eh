#!/bin/bash

# Lista todos los binarios del sistema con permiso SUID

find / -perm /4000 2>/dev/null
