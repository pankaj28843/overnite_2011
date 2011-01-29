#include<stdio.h>
#include<stdlib.h>
int t,x,i,tempr[1000],kt[500],p,max,j;
int sort_function( const void *a, const void *b);
int main()
{
	scanf("%d",&t);
	for(i=0;i<t;i++)
	scanf("%d",&tempr[i]);

	qsort((void *)tempr, t, sizeof(int), sort_function);

	p=t/2;

	for(i=0,j=t-1;i<p&&j>p;i++,j--)
	{
	  if(i!=j)
	  kt[i]=tempr[i]+tempr[j];

	}

	if(i==j)
	kt[i]=tempr[i];
	else
	 kt[i]=tempr[i]+tempr[j];



	max=kt[0];
	for(i=0;i<p;i++)
	{
	if(kt[i]>max)
	max=kt[i];
	}


	printf("\n%d",max);
return 0;
}
int sort_function( const void *a, const void *b)
{
	int x = *(int*)a;
	int y = *(int*)b;

	return (x-y);
}
