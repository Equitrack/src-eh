# Permisos especiales en Linux

## Sticky Bit

Los elementos que hay un directorio Sticky Bit, solo pueden ser renombrados o borrados por su propietario o bien por root. <br>
El resto de usuarios que tengan permisos de lectura y escritura, los podrán leer y modificar, pero no borrar. <br>

### Activación

Se puede activar utilizando:<br>
chmod 1775 test <br>
o bien <br>
chmod +t /test #para activar sticky bit <br>
chmod -t /test #para desactivar sticky bit <br>

## SUID

Es el acrónimo de set user id. <br>

[pcm@sal]$ ls -lh /usr/bin/passwd <br>
-rwsr-xr-x 1 root root 28K 2007-02-27 08:53 /usr/bin/passwd <br>

La s, que debería ser una x. indica el que programa se ejecutará con los privilegios del propietario, en lugar del usuario que lo ejecuta. <br>

Si se hace un mal uso de ellos y el propietario tiene privilegios, root. Se puede hacer una escala de privilegios.

### Activación del permiso SUID

[pcm@sal]$ chmod 4755 miprograma <br>
SUID es el bit más significativo, para los permisos espciales <br>
Estaremos activando el permiso SUID y estableciendo los permisos 755 al ejecutable miprograma. <br>

### Importante
La activación de SUID funciona solo con binarios y no con scripts (excepto con los de PERL). <br>
Este permiso no tiene efecto en los directorios.

### GTFObins

GTFOBins es una lista seleccionada de binarios de Unix que se pueden utilizar para eludir las restricciones de seguridad locales en sistemas mal configurados.

## SGUID
El bit SGID es lo mismo que SUID, pero a nivel de grupo. Esto es, todo archivo que tenga activo el SGID, al ser ejecutado, <br>
tendrás los privilegios del grupo al que pertenece. <br>
Es bastante útil si queremos configurar un directorio para colaborar diferentes usuarios. <br>

### Activación
chmod g+s "directorio" <br>
chmod 2555 "fichero" <br>

