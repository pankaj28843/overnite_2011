#include<stdio.h>

void main()
{

int t=0,i,j,temp,max=0,cou=0;
int ar[5000] ;
	scanf("%d",&t);

		for( i=1;i<=t;i++)
	{
	    scanf("%d",&ar[i-1]);

	   }
	   printf("\n");
	   cou=t-1;
	   for(i=0;i<(t-1);i++)
	   {
	       for(j=i+1;j<t;j++)
	       {
		   if(ar[j]>ar[i])
		   {
		       temp=ar[i];
		       ar[i]=ar[j];
		       ar[j]=temp;
		   }}}
		      max=-1111;
		   for(i=0;i<(t/2);i++)
		   {
		       if((ar[i]+ar[cou])>max)
		       max=ar[i]+ar[cou];
		       cou--;

		   }
		   if(ar[(t/2)+1]>max)

		   max=ar[(t/2)];
		  printf("%d",max);
		  printf("\n");

	       }
