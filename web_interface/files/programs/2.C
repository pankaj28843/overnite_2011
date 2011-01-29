#include<stdio.h>
#define MAX 1000
void swap(int a[],int x,int n);
int calSum(int a[],int n)
{
	int temp1=a[0],i,k,j;
	int temp2=a[0];
	if(n>=3){
	for(i=0;i<n;i++)
	{
		if(temp1<a[i+1]){k=i+2;
			temp1=a[i+1];}
		if(temp2>a[i+1]){j=i+2;
			temp2=a[i+1];}
	}
	swap(a,k,n);
	swap(a,j,n-1);}
	return(temp1+temp2);
}
void swap(int a[],int x,int n)
{
	int temp=a[x];
	a[x]=a[n-1];
	a[n-1]=temp;
}
int main()
{
int n,a[MAX],max,sum[MAX/2],summax;
	int i,n1;
	scanf("%d",&n);
	n1=n;
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
		for(i=0,n;i<=(n1+1)/2&&n>=0;n=n-2,i++)
			sum[i]=calSum(a,n);
		summax=sum[0];
		for(i=0;i<=(n1+1)/2;i++)
		{
			if(summax<sum[i])
				summax=sum[i];
		}
	printf("\n%d",summax);
	return 0;
}


