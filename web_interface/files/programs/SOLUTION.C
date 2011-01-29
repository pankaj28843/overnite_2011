#include<stdio.h>
int main()
{
int i,j,n,arr[20],max,tmp;
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&arr[i]);
}
max=arr[0]+arr[1];
for(i=0;i<n;i++)
{
	for(j=0;j<n;j++)
	{
		if(i==j)
			continue;
		tmp=arr[i]+arr[j];
		if(max<tmp)
		{
			max=tmp;
		}

	}

}
printf("%d",max);

return 0;
}