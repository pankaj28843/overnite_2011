#include<stdio.h>
#include<malloc.h>


int main()
{
int Acount,k,j,temp,i,max,max1,max2,even,step,p,value,count;
int * Array;
//clrscr();
scanf("%d",&Acount);



Array=(int *)malloc(sizeof(int)*(Acount+1));
for(i=1;i<=Acount;i++)
	scanf("%d",&Array[i]);
/*insert into heap*/
for(k=2;k<=Acount;++k)
{
	i=k;
temp=Array[k];
j=i/2;
while(i>1 && temp>Array[j])
{
	Array[i]=Array[j];
	i=j;
	j=i/2;
if(j<1)
	j=1;
}//end while
Array[i]=temp;
}//end for

// heap_sort(int list[],int n)
 //{
   //	int k,temp,value,j,i,p;
     //	int step=1;
	for(k=Acount;k>=2;--k)
	{
		temp=Array[1];
		Array[1]=Array[k];
		Array[k]=temp;
		i=1;
		value=Array[1];
		j=2;
		if((j+1)<k)
		if(Array[j+1]>Array[j])
		j++;
		while((j<=(k-1)&& (Array[j]>value)))
		{
			Array[i]=Array[j];
			i=j;
			j=2*i;
			if((j+1)<k)
			if(Array[j+1]>Array[j])
			j++;
			else
				if(j>Acount)
				j=Acount;
				Array[i]=value;
		}
}
for(i=1;i<=Acount;i++)
max1=Array[1];
if(Acount%2==1)
{
	count=1;
}
for(i=1;i<=Acount-count;i++)
{
step=Array[i]+Array[Acount-i-count+1];
if(step>max1)
	max1=step;
}

printf("max1%d",max1);
if(count==1)
{
	if(max1<Array[Acount])
		max1=Array[Acount];
}
printf("max1%d",max1);
max2=Array[1];//+Array[Acount];
for(i=1;i<=Acount ;i++)
{
if(i==Acount/2+1)
	continue;
step=Array[i]+Array[Acount-i+1];
if(step>max2)
	max2=step;
}



printf("%d\n",max2>max1?max1:max2);




/*
}
Array[Acount]=0;
max=Array[0]+Array[1];
if(Acount%2)
	even=1;
for(i=0;i<Acount;i=i+2)
{
	sum=(Array[i]+Array[i+1]);
	if(max>sum)
		max=sum;
}

printf("%d",SecondMax(Array,Acount));
return 0;
*/
return 0;
}
/* heap_sort(int list[],int n)
 {
	int k,temp,value,j,i,p;
	int step=1;
	for(k=Acount;k>=2;--k)
	{
		temp=Array[1];
		Array[1]=Array[k];
		Array[k]=temp;
		i=1;
		value=Array[1];
		j=2;
		if((j+1)<k)
		if(Array[j+1]>Array[j])
		j++;
		while((j<=(k-1)&& (Array[j]>value))
		{
			Array[i]=Array[j];
			i=j;
			j=2*i;
			if((j+1)<k)
			if(Array[j+1]>Array[j])
			j++;
			else
				if(j>n)
				j=n;
				Array[i]=value;
		} */