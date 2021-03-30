#include <stdio.h>

void main(){
   setuid(0);

   printf("Ejecutando (/usr/bin/ps): ruta absoluta\n");
   system("/usr/bin/ps");
   printf("Ejecutando (ps): ruta realtiva\n");
   system("ps");

}
