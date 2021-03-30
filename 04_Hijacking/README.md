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

## Creando binario


