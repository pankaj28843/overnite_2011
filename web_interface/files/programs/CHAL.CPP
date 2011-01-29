#include<iostream.h>
#include<complex.h>

void main()
{
	clrscr();
	cout<<"number of players\n";
	int n,ti;
	cin>>n;    //n cannot exceed 10
	int a[10];
	float sum=0;
	for(int i=0;i<n;i++)
	{
		cout<<"enter temper coefficient\n";
		cin>>a[i];
		sum+=a[i];
	}
	cout<<"sum="<<sum<<"\n";
	float avg= (sum*2)/n;
	cout<<"avg="<<avg<<"\n";
	int b[100];
	int h=0;
	for(int j=0;j<(n-1);j++)
	for(int k=j+1;j<n;j++)
		{

			{
			 b[h]=a[j]+a[k];
			 cout<<b[h];
			 h++;
			 }
		}
      cout<<"\n";
      float sub[10];

      for(i=0;i<h;i++)
      {
		sub[i]=abs(b[i]-avg);
      }
      float val[10];
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

      for( i=0;i<3;i++)   //3 to b n/2 for even
      for( j=0;j<h;j++)
      if(sub[i]==val[j])
      cout<<b[j]<<" " ;                    //max from b[j]

      cout<<"\n";
      int t;
     for(int d=0;d<3;d++)
     for(int s=0;s<3;s++)
     if(b[d]<b[s])
     {
     t=b[d];
     b[d]=b[s];
     b[s]=t;
     }
cout<<"max is"<<b[0];


}


