#include<stdio.h>
#include<stdlib.h>
int S,e,pools,c[50],b[50],minval[50],arr[50],i,high,visited[10],item=0;
int sort_function( const void *a, const void *b);

int notall()
{
	int p=1;
	for(i=0;i<pools;i++)
	{
	if(visited[i]==0)
	p=0;
	}
return p;
}

int max()
{
	int max;
	max=minval[0]/b[0];
	high=0;

	for(i=0;i<pools;i++)
	{
	if((minval[i]/b[i])>max&&visited[i]!=1)
	{
	max=minval[i]/b[i];
	high=i;
	}

	}
return minval[high];
}

int min()
{
	int min,high2=0;
	min=minval[0]/b[0];

	for(i=0;i<pools;i++)
	{
	if((minval[i]/b[i])<min&&visited[i]!=1)
	{
	min=minval[i]/b[i];
	high2=i;
	}

	}
return minval[high2];
}



int main()
{
	int cost=0,k,high1;
	scanf("%d %d",&S,&e);
	scanf("%d",&pools);

	for(i=0;i<pools;i++)
	scanf("%d %d",&c[i],&b[i]);

	for(i=0;i<pools;i++)
	{
	minval[i]=(b[i]*e+b[i]*c[i]);
	}


	while(1)
	{
	  if(notall())
	  break;

	  k=max();
	  cost=cost+k;
	  item=item+b[high];

	  if(cost>S)
	  {
	  cost=cost-k;
	  item=item-b[high];
	  visited[high]=1;
	  }
	  else
	  {

	  while(cost<=S)
	  {
	   cost=cost+c[high]+e;
	   item++;
	  }
	  visited[high]=1;

	  if(cost>S)


	  if(cost>S)
	  {

	  high1=high;
	  do
	  {
	  cost=cost-c[high1]-e;
	  item=item-1;
	  }while(((cost+min()>=S)||cost>S)&&!notall());


	  }

	  }


	  }


	if(item==0)
	printf("\n-1");
	else
	printf("\n%d",item);
	return 0;
}


