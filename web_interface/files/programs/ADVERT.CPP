#include<stdio.h>
#include<stdlib.h>
int t,x,i,tempr[100],kt[50],p,max;
int sort_function( const void *a, const void *b);
int main()
{
	scanf("%d",&t);
	for(i=0;i<t;i++)
	scanf("%d",&tempr[i]);

	qsort((void *)tempr, t, sizeof(int), sort_function);

	if(t%2==0)
	p=t/2;
	else
	p=(t-1)/2;

	for(i=0;i<p;i++)
	{
	  kt[i]=tempr[i]+tempr[i+1];
	}

	max=kt[0];
	for(i=0;i<p;i++)
	{
	if(kt[i]>max)
	max=kt[i];
	}

	printf("%d",max);
return 0;
}
int sort_function( const void *a, const void *b)
{
	int x = *(int*)a;
	int y = *(int*)b;

	return (x-y);
}
