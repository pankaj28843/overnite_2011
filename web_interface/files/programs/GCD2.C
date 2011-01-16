// DEBANJAN SAHA--663937

#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
void main()
{
int n,a,b,z,i,f[30];
clrscr();
printf("INPUT\n");
scanf("%d",&n);
printf("\n");
for(i=0;i<n;i++)
{
scanf("%d %d",&a,&b);
printf("\n");
while(b>0)
{
z=a%b;
a=b;
b=z;
}
f[i]=a;
}
printf("\n\nOUTPUT\n");
for(i=0;i<n;i++)
{
printf("%d\n",f[i]);
}
getch();
}
