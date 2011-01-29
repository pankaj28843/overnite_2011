#include<stdio.h>
#include<stdlib.h>

int main()
{
long int n,k,sum=0,a=0,b=1,i;

long int *ti;
scanf("%ld %ld", &n,&k);
ti = (long int *)malloc(sizeof(long int)*n);
for (i = 0; i < n; i++) {
	scanf("%ld", &ti[i]);

}
for(i=0;i<k;i++)
{
sum+=ti[b]-ti[a];
a+=2;
b+=2;
}
sum*=2;
printf("%ld\n",sum);
return 0;
}





