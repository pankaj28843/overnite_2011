#include<stdio.h>
void main()
{
int n,m,k,xd,yd,p,xo[50],yo[50],i,result=0,x,y,j=0;
int road[100][100],poss=1,poss1=1,poss2=1;
scanf("%d%d%d",&n,&m,&k);
scanf("%d%d",&yd,&xd);
scanf("%d",&p);
for(i=0;i<p;i++)
{
scanf("%d%d",&yo[i],&xo[i]);
}
for(i=0;i<n;i++)
{
for(j=0;j<m;j++)
{
road[i][j]=1;
}}
for(i=0;i<p;i++)
{
x=xo[i]-1;
y=yo[i]-1;
road[x][y]=0;
}
for(i=0;i<n;i++)
if(road[i][0]!=1)
{
poss=0;
}
for(i=0;i<yd;i++)
{
if(road[xd-1][i]!=1)
poss1=0;
}
for(i=0;i<xd;i++)
if(road[i][yd-1]!=1)
poss2=0;
if(poss==1)
{
if(poss1==1)
result=result+1;
if(poss2==1)
result=result+1;
}
printf("%d",result);
}


