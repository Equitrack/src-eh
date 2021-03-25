# Grupos
Los grupos sirven para organizar un conjunto de usuarios, y gestionar de mejor manera los permisos en los ficheros y directorios del sistema. <br>

- Crear grupo
```
gropadd <nombreGrupo>
```
- Cambiar el grupo de un directorio/fichero
```
chgrp <nombreGrupo> <nombredirectorio>
```
- Agregar un usuario a un grupo
```
usermod -a -G <nombreGrupo> <nombreUsuario>
```
