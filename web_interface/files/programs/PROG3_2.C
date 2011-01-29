#include<stdio.h>
//#include<malloc.h>

struct pair
{
	int a,b,dist;
};

struct pair p_no[100005];

int compitible(int x, int y)
{
	 if(p_no[x].b == p_no[y].a || p_no[x].a == p_no[y].b)
		 return 0;
	 else
		 return 1;
}

int max(int a,int b)
{
	if(a > b)
	{
		return a;
	}else
		 {
			 return b;
		 }
}

int main()
{
	int i,n,k,*arr, value = 0, loop, min11 = -1,min12 = -1, min21 = -1, min22 = -1,result = 0, j;


	arr = (int*)malloc(sizeof(int)*(n+5));

	scanf("%d %d",&n,&k);

	for(i=0;i<n;i++)
	{
		 scanf("%d",&arr[i]);
	}

	 //adjacent pair 1
		  for(i=0;i+1<n;i=i+2)
		  {
			  p_no[value].a = i;
			  p_no[value].b = i+1;
			  p_no[value].dist = arr[i+1]-arr[i];

			  if(min11 == -1)
			  {
					min11 = p_no[value].dist;
			  }else if(min12 == -1)
					  {
							min12 = p_no[value].dist;
					  }else{
								  if(max(min11,min12) > p_no[value].dist)
								  {
									  if(min11 > min12)
									  {
											min11 = p_no[value].dist;
									  }else{
												 min12 = p_no[value].dist;
											 }
								  }
							 }
			  value++;
		  }

	 //adjacent pair 2
		  for(i=1;i<n;i=i+2)
		  {
			  p_no[value].a = i;
			  p_no[value].b = i+1;
			  p_no[value].dist = arr[i+1]-arr[i];


			  if(min21 == -1)
			  {
					min21 = p_no[value].dist;
			  }else if(min22 == -1)
					  {
							min22 = p_no[value].dist;
					  }else{
								  if(max(min21,min22) > p_no[value].dist)
								  {
									  if(min21 > min22)
									  {
											min21 = p_no[value].dist;
									  }else{
												 min22 = p_no[value].dist;
											 }
								  }
							 }
			  value++;
		  }


	 if(min11+min12 > min21+min22)
	 {
		 result = min21+min22;
	 }else{
				 result = min11+min12;
			}

	 for(i = 0;i < n/2;i++)
	 {
		 for(j = 0;j < n/2;j++)
		 {
			  if(compitible(i,j+(n/2)))
			  {
				 if(result > (p_no[i].dist + p_no[j+(n/2)].dist))
				 {
					  result = (p_no[i].dist + p_no[j+(n/2)].dist);
				 }
			  }
		 }
	 }//end i loop

	 printf("\n%d",result+result);

	return 0;
} //end fo amaoni