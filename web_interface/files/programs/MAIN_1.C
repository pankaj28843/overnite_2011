#include<stdio.h>
#include<stdlib.h>




int cmp1(long int *p1,long int *p2){
if(*p1<*p2)return -1;
if(*p1==*p2)return 0;
return 1;

}



int main()
{
long int n,i,a,b,c=0,d=0,j,k,left,right;
long int *ti,*pair1,*pair2,max1,max2,max3,max;
scanf("%ld", &n);
		if (!n) {
			return 0;
		}

		ti = (long int *)malloc(sizeof(long int)*n);
		for (i = 0; i < n; i++) {
			scanf("\n%ld", &ti[i]);

		}
		qsort(ti,n,sizeof(long int),(int (*)(const void *,const void *))cmp1);
		pair1 = (long int *)malloc(sizeof(long int)*(n/2));
		pair2 = (long int *)malloc(sizeof(long int)*(n/2 + 1));

		if(n % 2 ==0)
		{
			j=n/2;
			i=n/2 -1;
			k=n/2;
			for(j=0;j<n/2;j++)
			{
			a= ti[i];
			b= ti[k];
			pair1[c]=a+b;
			i--;
			k++;
			c++;
			}
		max1=pair1[0];
		for(j=0;j<c;j++)
		{
		if(pair1[j]>max1)
			max1=pair1[j];
		}
		printf("%ld\n",max1);
		}
		
		else
		{
			c=0;
			j=n/2;
			i=n/2;
			k=n/2+1;
			for(j=0;j<n/2;j++)
			{
			a= ti[i];
			b= ti[k];
			pair2[c]=a+b;
			i--;
			k++;
			c++;
			}
			max1=ti[0];
			for(j=0;j<c;j++)
			{
			if(pair2[j]>max1)
				max1=pair2[j];
			}
			
			c=0;
			j=n/2;
			i=n/2 -1;
			k=n/2;
			for(j=0;j<n/2;j++)
			{
			a= ti[i];
			b= ti[k];
			pair2[c]=a+b;
			i--;
			k++;
			c++;
			}
			max2=ti[n-1];
			for(j=0;j<c;j++)
			{
			if(pair2[j]> max2)
				max2=pair2[j];
			}
			
			c=0;
			j=n/2;
			i=0;
			k=n-1;
			for(j=0;j<n/2;j++)
			{
			a= ti[i];
			b= ti[k];
			pair2[c]=a+b;
			i++;
			k--;
			c++;
			}
			max3=ti[n/2];
			for(j=0;j<c;j++)
			{
			if(pair2[j]> max3)
				max3=pair2[j];
			}

			if(max1<max2 && max1<max3)
					max=max1;
			if(max2<max1 && max2<max3)
					max=max2;
			if(max3<max1 && max3<max2)
					max=max3;
			printf("%ld\n",max);

			
			
		
		}
	
	return 0;
}