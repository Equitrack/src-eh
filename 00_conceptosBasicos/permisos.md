# Permisos

Cada fichero y directorio de linux contiene permisos. <br>
Estos persmisos son:
- Lectura	-	r [read]	
- Escritura	-	w [write]
- Ejecución	-	x [execute]

Ejemplo:
```
$ ls -l
-rw-r--r--. 1 tony tony 167 Mar 24 21:31 permisos.md
```

[-rw-r--r--.] <br>
El primer caracter representa si es un directorio [d] o no [-]. <br>
Las tercias de carácteres, se asignan de la siguiente forma:

- Usuario propietario	-	u [user]
- Grupo de usuarios	-	g [group]
- Otros usuarios	-	o [others]

Cada tercia contiene los permisos. 

[-rw-r--r--. 1 tony tony] <br>
Lo siguiente es el propietario del archivo, y lo segundo al grupo al que pertenece. <br>
Por defecto al crear ficheros en el directorio /home/$user, asignará el grupo del propietario.<br>

## Cambio de permisos

Si se es el propietario de un fichero, o el usuario root. Se pueden modificar los archivos. <br>
El comando para modificar los archivos es <strong>chmod</strong> <br>

Ejemplos:
- Agregar permiso de ejecución[x] al propietario[u]
```
chmod u+x <nombre del fichero>

u: representa al usuario propietario
x: representa el permiso de ejecución
```
- Agregar permiso de lectura[r] a otros[o], es decir: el usuario que no es propietario, y tampoco se encuentra dentro del grupo del fichero.
``` 
chmod o+r <nombre del fichero>
```

Si nuestro archivo tiene la siguiente estructura al ejecutar '$ ls -l': <br>
-rw-r--r--. 1 tony desarrolladores 1.5K Mar 24 21:53 permisos.md <br>
- Para quitar permiso de escritura[w] al grupo desarrolladores[g] <br>
```
chmod g-w <nombre del archivo>
```

También se pueden hacer estas operaciones de cambio de permisos separando por comas cada una:
```
chmod u+r, g-x, o-w <nombre del fichero>
```
