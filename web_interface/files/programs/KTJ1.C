#include<stdio.h>
#include<limits.h>
int main()
{ int n,i,j,temp,*ti,sum=INT_MIN;
  scanf("%d",&n);
  ti=(int*)malloc(n*sizeof(int));
  for(i=0;i<n;i++)
  scanf("%d",&ti[i]);
  for(i=0;i<n;i++)
  {for(j=0;j<n-i-1;j++)
   { if(ti[j]>ti[j+1])
     { temp=ti[j];
	ti[j]=ti[j+1];
	ti[j+1]=temp;
     }
   }
  }
  for(i=0;i<(n/2);i++)
  {   if(sum<(ti[i]+ti[n-1-i]))
      sum=ti[i]+ti[n-1-i];
  }
  if(n%2!=0)
  { if(sum<ti[i]);
    sum=ti[i];
  }
  printf("%d",sum);
  return 0;
}
