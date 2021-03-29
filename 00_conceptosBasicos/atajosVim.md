# Atajos de vim
[Desplazamiento en el documento]
j	abajo
k	arriba
h	izquierda
l	derecha

[Posicionar cursor]
a	posicionar cursor deltante del cararacter
i	posicionar cursos atras del caracter

[Cambios en el texto]
x	eliminar caracter
u	dehacer último cambio

[Guardar cambios]
:w	guardar cambios
:q	salir
:x	salir y guardar

[Moverse entre archivos]
gd	ir a la definición
gf	ver la definición
Ctrl+o 	ir hacía atrás del historial
Ctrl+i	ir hacía adelante del historial

[Eliminar texto]
dw	delete word
u	deshacer, undo
Ctrl+r	rehacer, redu
dd	elimina toda la linea
de	eliminat desde el cursor hasta el final de linea

[Moverse entre palabras]
w	moverse una palabra hacía adelante, word
b	moverse una palabra hacia atrás, back
7w	7 words
4b	4 back

[Clipboard]
Aquí se guarda lo que se elimina dentro de vim.
p	pegar el texto eliminado, una linea debajo del cursor
P	pegar en la linea de arriba

[Operador de cambios]
cw	change word, borrar palabra
ciw	change intern word

[Moverse entre el archivo]
gg	Ir al comiendo del archivo
G	Ir al final de un archivo

[Búsqueda]
/<Palabra> búsqueda de la palabra después del cursor, presionar n para el siguiente y N para el anterior
?<Palabra> búqueda de la palabra antes del cursor, presionar n para el siguiente y N para el anterior

[Ir al parentesis de inicio y final]
%	El cursor se mueve hasta donde cierra o abre el paréntesis que tiene el cursor
%c	borra el contenido de los paréntesis y los paréntesis

[Sustituir una cadena de texto]
:s/orignal/nuevo/g	Solo para la linea en la que se encuentra el cursor
:%s/origial/nuevo/g	Para todo el fichero
:%s/origial/nuevo/gc	Para todo el fichero, pero pregunta si se aplica, pasando por cada palabra

[Abrir nuevas lineas]
o	nueva linea abajo
O	nueva linea arriba
R	rermplazar texto, de forma indefinida

[Modo visual]
:v	abre el modo visual
y	Copiar texto

