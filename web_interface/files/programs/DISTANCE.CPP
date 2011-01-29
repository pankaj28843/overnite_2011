#include<stdio.h>
#include<conio.h>
int main()
{
 int d[100],d1[100],a[100][2],n,k,i,j,temp,add[100],min,pos;
 scanf("%d%d",&n,&k);
 for(i=0;i<n;i++)
 {
  scanf("\n%d",&d[i]);
 }
 for(i=0;i<n-1;i++)
 {
  d1[i]=d[i+1]-d[i];
  a[i][0]=d[i];
  a[i][1]=d[i+1];
 }
 for(i=0;i<n-1;i++)
 {
  for(j=0;j<n-1-i;j++)
  {
   if(d1[j]>d1[j+1])
   {
    temp=d1[j];
    d1[j]=d1[j+1];
    d1[j+1]=temp;
    temp=a[j][0];
    a[j][0]=a[j+1][0];
    a[j+1][0]=temp;
    temp=a[j][1];
    a[j][1]=a[j+1][1];
    a[j+1][1]=temp;
   }
  }
 }
 pos=0;
 for(i=0;i<n-2-l;i++)
 {
  for(j=i+1;j<n-1;j++)
  {
   if(a[i][0]!=a[j][0] && a[i][0]!=a[j][1] && a[i][1]!=a[j][0] && a[i][1]!=a[j][1])
   {
    add[pos]=d1[i]+d1[j];
    pos++;
   }
  }
 }
  //min function
  min=add[0];
  for(i=1;i<pos;i++)
  {
  if(min<add[i])
  min=add[i];
  }
  printf("\n%d",min*2);
  getch();
  return 0;
}