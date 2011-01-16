#include<stdio.h>
int pos=0;
float sum=0;


void boom(int start, char string[], int pos)
{
	int remember=start;
	int rememberpos=pos;
	start=start*2;
	do
	{       pos=pos+1;
		switch(string[pos])
		{
		case 'L':
			start=start*2;
			break;
		case 'R':
			start=(start*2)+1;
			break;
		case 'P':
			break;
		case '\0':
			sum=sum+start;

			break;
		case '*':
			 boom(start,string,pos);
			 break;
		}

	}        while(string[pos]!='\0');
	start=remember;
	pos=rememberpos;
		start=(start*2)+1;
	do
	{       pos=pos+1;
		switch(string[pos])
		{
		case 'L':
			start=start*2;
			break;
		case 'R':
			start=(start*2)+1;
			break;
		case 'P':
			break;
		case '\0':
			sum=sum+start;

			break;
		case '*':
			 boom(start,string,pos);
			 break;
		}
	}     while(string[pos]!='\0');
	start=remember;
	pos=rememberpos;
		do
	{       pos=pos+1;
		switch(string[pos])
		{
		case 'L':
			start=start*2;
			break;
		case 'R':
			start=(start*2)+1;
			break;
		case 'P':
			break;
		case '\0':
			sum=sum+start;

			break;
		case '*':
			 boom(start,string,pos);
			 break;
		}
	}     while(string[pos]!='\0');

};


int main()
{
	int t;
	scanf("%d",&t);
	char line[10001];
	int val=1;
	for(int i=0;i<t;i++)
	{
	gets(line);
	val=1;
	sum=0;
	pos=0;
	while(line[pos]!='\0')
	{

	switch(line[pos])
	 {
	 case 'L':
		val=val*2;
			break;
		case 'R':
			val=(val*2)+1;
			break;
		case 'P':
			break;
		case '\0':
			sum=sum+val;
			break;
		case '*':
			 boom(val,line,pos);
	 }
	 pos=pos+1;

	}
	printf("%f\n",sum);
	}
	printf("\n");
	return (0);
}
