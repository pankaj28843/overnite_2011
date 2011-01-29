#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void main()
{
 int t,i,k,row, col,sum,temp[50],j,n,n1,b[50][50],nop,a[50];
 cout<<"Enter the no. of Players: ";
 cin>>nop;
 for(i=0;i<nop;i++)
 {
  for(j=0;j<nop;j++)
  {
   b[i][j]=5000;
  }
 }
 if((nop%2)!=0)
 {
  for(i=0;i<nop;i++)
  {
   cin>>a[i];
  }
 nop--;
 }
 else
 {
 for(i=0; i<nop; i++)
 {
  cin>>a[i];
 }
 }
 //m=0;
 for(i=0;i<nop-1;i++)
 {
  for(j=i;j<nop-1;j++)
  {
   n1=a[i]-a[j+1];
   int n=abs(n1);
   b[i][j]=n;
  // cout<<b[i][j]<<" ";
  }
 // cout<<"\n";
 }
 t=b[0][0];
 for(i=0;i<nop-1;i++)
 {
  for(j=i;j<nop-1;j++)
  {
   if(t>b[i][j])
   {
    t=b[i][j];
    row=i;
    col=j;
   }
  }
 }
 sum=a[row]+a[col+1];
 cout<<"The output is: "<<sum<<"\n";
 //cout<<t;
 getch();
}

