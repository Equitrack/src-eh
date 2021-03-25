# Permisos

Cada fichero y directorio de linux contiene permisos. <br>
Estos persmisos son:
- Lectura	-	r [read]	
- Escritura	-	w [write]
- Ejecución	-	x [execute]

Ejemplo:
```
-rw-r--r--. 1 tony tony 167 Mar 24 21:31 permisos.md
```

[-rw-r--r--.]
El primer caracter representa si es un directorio [d] o no [-]. <br>
Las tercias de carácteres, se asignan de la siguiente forma:

- Usuario propietario
- Grupo de usuarios
- Otros usuarios

Cada tercia contiene los permisos. 

[-rw-r--r--. 1 tony tony]
Lo siguiente es el propietario del archivo, y lo segundo al grupo al que pertenece.
Por defecto al crear ficheros en el directorio /home/$user, asignará el grupo del propietario.
