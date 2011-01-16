#include<stdio.h>
#include<Conio.h>
#include<math.h>
int gcd(int d,int e)
{  if(e!=0)
      {
       d=d%e;
       return gcd(e,d);
      }
     else
       return(d);
}

void main()
{
double i,a,b[100],c[100],d,e,f;
clrscr();
scanf("%lf",&a);
for(i=0;i<a;i++)
{
scanf("%lf%lf",&b[i],&c[i]);
if(b[i]>c[i])
{f=b[i];
b[i]=c[i];
c[i]=f;
}
}
for(i=0;i<a;i++)
{
d=b[i];
e=c[i];
f=gcd(d,e);
printf("%lf\n",f);
}
getch();
}