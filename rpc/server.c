#include <stdio.h>
#include "teste.h"

/* implementação da função som */
int * som_1_svc (operands *argp, struct svc_req *rqstp)
{
   static int result;

   printf ("Recebi chamado: add %d %d\n", argp->x, argp->y);
   result = argp->x + argp->y;
   return (&result);
}

/* implementação da função mut */
int * mut_1_svc (operands *argp, struct svc_req *rqstp)
{
   static int result;

   printf ("Recebi chamado: sub %d %d\n", argp->x, argp->y);
   result = argp->x * argp->y;
   return (&result);
}


/* implementação da função div */
int * divi_1_svc (operands *argp, struct svc_req *rqstp)
{
   static int result;

   printf ("Recebi chamado: add %d %d\n", argp->x, argp->y);
   result = argp->x / argp->y;
   return (&result);
}

/* implementação da função sub */
int * sub_1_svc (operands *argp, struct svc_req *rqstp)
{
   static int result;

   printf ("Recebi chamado: sub %d %d\n", argp->x, argp->y);
   result = argp->x - argp->y;
   return (&result);
}

/* implementação da função mod */
int * mod_1_svc (operands *argp, struct svc_req *rqstp)
{
   static int result;

   printf ("Recebi chamado: add %d %d\n", argp->x, argp->y);
   result = argp->x % argp->y;
   return (&result);
}

/* implementação da função pot */
int * pot_1_svc (operands *argp, struct svc_req *rqstp)
{
   static int result;

   printf ("Recebi chamado: sub %d %d\n", argp->x, argp->y);
   int cont;
   for(int i = 0; i < argp->x; i++){
      cont = i * argp->y;
   }
   result = (cont);
   return (&result);
}

int * raiz_1_svc (operands *argp, struct svc_req *rqstp)
{
   static int result;

   printf ("Recebi chamado: sub %d %d\n", argp->x, argp->y);
   result = (argp->x);
   return (&result);
}
