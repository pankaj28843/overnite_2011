#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define MAXNO 100 
#define EXCH(X,Y,Z) ((Z)=(X), (X)=(Y), (Y)=(Z))
void selectionSort(int [], int);
int main() // main.c
{
    int no , i ;
    int data[MAXNO] ;
 
    scanf("%d",&no);
    for(i=0;i<no;i++)
       scanf("%d", &data[i]);
    selectionSort(data, no) ;
    for(i = 0; i < no; ++i)
    {
      printf("%d\t", data[i]);
    }
    putchar('\n') ;
    return 0 ;
}
void selectionSort(int data[], int nod)
 { 
     int i ;

     for(i = 0; i < nod - 1; ++i) {
         int max, j ;
         int temp ;

         temp = data[i] ;
         max = i ;
         for(j = i+1; j < nod; ++j)
             if(data[j] > temp) {
                temp = data[j] ;
                max = j ;
             }
         EXCH(data[i], data[max], temp);
     }
}

