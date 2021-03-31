#include <stdio.h>

void main(){

   setuid(0);

   printf("Ejecutando con el usuario: (/usr/bin/whoami): ruta absoluta\n");
   system("/usr/bin/whoami");

   printf("Ejecutando con el usuario: (whoami): ruta realtiva\n");
   system("whoami");
}
