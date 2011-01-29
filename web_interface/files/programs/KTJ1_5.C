#include<stdio.h>
#include<malloc.h>
#define EXCH(X,Y,Z) ((Z)=(X), (X)=(Y), (Y)=(Z))
int main()
{ int n=6,i,j,max,temp,*ti,sum;
  scanf("%d",&n);
  ti=(int*)malloc(n*sizeof(int));
  for(i=0;i<n;i++)
  scanf("%d",&ti[i]);
  for(i = 0; i < n - 1; ++i)
  {temp = ti[i];   
   max = i ;
   for(j = i+1; j < n; ++j)
   if(ti[j] > temp)
  { temp = ti[j] ;    
    max = j ;             
  } 
    EXCH(ti[i], ti[max], temp);
  }
  sum=ti[0]+ti[n-1];
  for(i=1;i<(n/2);i++)
  {   if(sum<(ti[i]+ti[n-1-i]))
      sum=ti[i]+ti[n-1-i];
  }
  if(n%2!=0)
  { if(sum<ti[i])
    sum=ti[i];
  }
  printf("%d",sum);
  return 0;
}