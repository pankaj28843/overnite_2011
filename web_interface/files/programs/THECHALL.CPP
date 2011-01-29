#include<stdio.h>

#include<iostream.h>


void main()
{

int i,no_pl,ti[10],max1,sum=0,sum1=0;
float asum;
int maxm,min,maxa[100];             //a team can have a max of 10 playrs
cout<<"enter the number of players";
cin>>no_pl;
   cout<<"enter the ti of players";
for(i=0;i<no_pl;i++)
{ cin>>ti[i];
	  sum1=sum1+ti[i];
}


for(i=0;i<no_pl;i++)
{
 for(int j=i+1;j<no_pl;j++)
      { max1= ti[i]+ti[j];
	 sum=sum+max1;

	   }

}


  asum= sum/sum1 ;
  maxm=ti[0]-asum;
  for(i=0;i<no_pl;i++)
{
min = ti[i]-asum;
if( min <maxm)
{maxm=min;
}

}
 cout<<"the max compat is";
 cout<< maxm;

}


