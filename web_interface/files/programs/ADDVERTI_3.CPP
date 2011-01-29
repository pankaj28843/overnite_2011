#include<iostream.h>
#include<conio.h>
#include<stdio.h>
int main()
{
	clrscr();
	int i,j,n,a[20],temp,tot,m,s[20],k;

	scanf("%d",&n);
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<(n-1)-i;j++)
		{
			if(a[j]>a[j+1])
			{
				temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
			}
		}
	}
	k=0;
	for(i=0,j=n-1;i<=j;i++,j--)
	{
		if(i!=j)
		{
			s[k]=a[i]+a[j];
		}
		else
		s[k]=a[i];

		k++;
	}
	if(n%2==0)
	tot=n/2;
	else
	tot=(n/2)+1;
	m=s[0];
	for(i=1;i<tot;i++)
	{
		if(s[i]>m)
		m=s[i];
	}
	printf("%d",m);

	getch();
	return 0;
}


