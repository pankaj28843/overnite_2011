#include<stdio.h>
int main()
{
int n,k,i,j,l,sw=0;
char comb[60][60];
scanf("%d %d %d",&n,&k,&i);
for(j=0;j<i;j++)
{
	for(l=0;l<n-j;l++)
	{
	comb[j][l]='N';
	}
	for(;l<n;l++)
	{
	comb[j][l]='O';
	}
}

for(j=0;j<n-1;j++){
if(comb[i-1][j]!=comb[i-1][j+1])
sw++;
}
l=-1;
if(sw>k)
{
	printf("%d",l);
}
else{
for(j=0;j<n;j++){
	printf("%c",comb[i-1][j]);
}
}

return 0;
}