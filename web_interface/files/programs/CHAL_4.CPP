#include<iostream.h>
#include<complex.h>

void main()
{
	cout<<"number of players\n";
	int n,ti,max2;
	cin>>n;
	int a[10],sum=0;
	for(int i=0;i<n;i++)
	{
		cout<<"enter temper coefficient\n";
		cin>>a[i];
		sum+=a[i];
	}
	float avg= (sum*2)/n;
	int b[100],c[100];
	int h=0;
	for(int j=0;j<(n-1);j++)
	{for(int k=j+1;j<n;j++)

		 {
			 b[h]=a[j]+a[k];
			 h++;
			}
		}
      float sub[100];
      for(i=0;i<h;i++)
      {
		sub[i]=abs(b[i]-avg);
      }
      float val[100];
      for(int f=0;f<h;f++)
      {
      val[f]=sub[f];
      }

      float temp;
      for(j=0;j<h;j++)
      {
		for(int p=j;p<h;p++)
		 {
		 if(sub[j]>sub[p])
		 {
		 temp=sub[j];
		 sub[j]=sub[p];
		 sub[p]=temp;
		 }
		 }
		}
	 int l =0;
      for( i=0;i<3;i++)   //3 to b n/2 for even
  {    for( j=0;j<h;j++)
      if(sub[i]==val[j])
     { cout<<b[j];
     c[l]=b[j];
     l++;			 //max from b[j]
      }
   }

      max2=c[0];
       for(i=0;i<l;i++)
	{if(c[i]>max2)
	{ max2=c[i];
	 }
       }
	    cout<<"max cop is";
	    cout<<max2;

}





