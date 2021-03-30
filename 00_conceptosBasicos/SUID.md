# SUID

Es el acrónimo de set user id. <br>

[pcm@sal]$ ls -lh /usr/bin/passwd <br>
-rwsr-xr-x 1 root root 28K 2007-02-27 08:53 /usr/bin/passwd <br>

La s, que debería ser una x. indica el que programa se ejecutará con los privilegios del propietario, en lugar del usuario que lo ejecuta. <br>

Si se hace un mal uso de ellos y el propietario tiene privilegios, root. Se puede hacer una escala de privilegios.

## Activación del permiso SUID

[pcm@sal]$ chmod 4755 miprograma <br>
SUID es el bit más significativo, para los permisos espciales <br>
Estaremos activando el permiso SUID y estableciendo los permisos 755 al ejecutable miprograma. <br>

## Importante
La activación de SUID funciona solo con binarios y no con scripts (excepto con los de PERL). <br>
Este permiso no tiene efecto en los directorios.
