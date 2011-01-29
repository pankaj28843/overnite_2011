#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
void quick_sort(int [],int ,int ,int );
void split_array(int [],int ,int ,int*);

int recurse(int*dist,int k,int n)
 {
  int j,min,i;
  min=dist[0]+dist[2];
  if(k==2)
  {
   for(i=0;i<n-1;i++)
     {
       for(j=i+2;j<n-1;j++)
	 {
	   if(dist[i]+dist[j]<min)
	    {
	      min=dist[i]+dist[j];

	    }
	 }
     }
     return min;

   }
   else
    {
     return(recurse(dist+2,k-1,n-2)+dist[0]);
    }

 }

void main()
{
 int a[100],i,n,k,min=0;
 int dist[100],j=1,sum=0,swap[100],final[100];
 clrscr();
printf("\nenter the No of Players and no of players to be swapped:\n");
scanf("%d %d",&n,&k);

if(n>100)
 {
    printf("\Player number beyond access:\n");
    exit(1);
 }

 if(n<2*k)
   {
      printf("\nInvalid Input\n");
      exit(1);
   }


 printf("\nenter the Distances between Countries:\n");
 for(i=0;i<n;i++)
   scanf("%d",&a[i]);

 quick_sort(a,n,0,n-1);

 for(i=0;i<n-1;i++)
   {
     dist[i]=a[i+1]-a[i];

   }

   //min=dist[0]+dist[2];

   min=recurse(dist,k,n);
// quick_sort(final,j,0,j-1);

 //for(j=1;j<=k;j++)
   //   sum+=final[j-1];


      printf("\nOutput:\n%d",min*2);
      getch();

 // printf("\nthe array elements after sorting are as:-\n");
 // for(i=0;i<n;i++)
 //  printf("%d\t",a[i]);
 //printf("\n");


 }

void quick_sort(int a[],int n,int lb,int ub)
 {

  int loc;
  if(lb<ub)
  {
   split_array(a,lb,ub,&loc);
   quick_sort(a,n,lb,loc-1);
   quick_sort(a,n,loc+1,ub);
  }

 }

void split_array(int a[],int beg,int end,int*loc)

 {
  int left,right,done,temp;
      *loc=left=beg;
   right=end;
 done=0;
  while(!done)
  {
    while((a[right]>=a[*loc])&&(*loc!=right))
      right--;
    if(*loc==right)
      done=1;
    else
     {
	if(a[*loc]>a[right])
          {
	    temp=a[*loc];
	    a[*loc]=a[right];
	    a[right]=temp;
	    *loc=right;
          }
     }
   
    if(!done)
    {
      while((a[left]<=a[*loc])&&(*loc!=left))
        left++;
      if(*loc==left)
       done=1;
      else
       {
        if(a[*loc]<a[left])

         {
	   temp=a[*loc];
           a[*loc]=a[left];
	   a[left]=temp;
           *loc=left;
         }
       }
     }
   }
}


