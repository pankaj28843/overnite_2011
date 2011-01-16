// DEBANJAN SAHA--663937

#include<stdio.h>
#include<conio.h>
int gcd(int m,int o)
{
if(o==0)
return m;
else
gcd(o,m%o);
}
void main()
{
int n,a,b,i,f[30];
clrscr();
printf("INPUT\n");
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d %d",&a,&b);
f[i]=gcd(a,b);
}
printf("\n\nOUTPUT\n");
for(i=0;i<n;i++)
{
printf("%d\n",f[i]);
}
getch();
}
