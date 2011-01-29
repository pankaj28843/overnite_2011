#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>
int main()
{
 clrscr();
 int i,n,k,j,a,b,l,s=0;
 char *p[100],str[100];
 //printf("\nEnter the no. of balls(n<=60),no. of switches(k>=0) and the ith set\n");
 scanf("%d%d%d",&n,&k,&i);
 double c=pow(10,18);
 if(n>60 || k<0 || i>c)
 exit(0);

 //storing all valid combinations in tha pointer array 'p'
 for(j=0;j<=n;j++)
 {
  for(a=0;a<n-j;a++)
  str[a]='N';
  for(b=n-j;b<n;b++)
  str[b]='O';
 l=strlen(str);
p[j]=(char *)malloc(l);
strcpy(p[j],str);
}
strcpy(str,p[i-1]);
l=strlen(str);
for(a=0;a<l-1;a++)
{
 if(str[a]!=str[a+1])
 s++;
}
if(s!=k)
printf("%d",-1);
else
printf("\n%s",str);
getch();
return 0;
}