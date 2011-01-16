#include<stdio.h>
int gcd(int y,int x)
{
int z;
if(x%y==0)
return y;
z=x%y;
while(z!=0)
{
x=y;
y=z;
z=x%y;
}
return y;
}
int main()
{
        int num,k,t,a,i,b[1000],n,res,l,j;
        char s[1000];
        scanf("%d",&t);
        for(k=0;k<t;k++)
        {
        scanf("%d %s",&a,s);
        i=0;
        while(s[i]!= NULL)
         {
                b[i]=(int)s[i]; 
                b[i]-=48;
                i++;
         }
        l=i;
        num = 0;
        for(j=0;;j++)
        {
                num+=b[j];
                if(num>a)
                  break;
                num=num*10;
        }
        //printf("%d  %d\n",num,j);
        j++;
        while(j<l)
        {
                num=num%a;
                num*=10;
                num+=b[j];
                j++;    
        }
        res = num%a;
        //printf("%d  \n",res);
        res = gcd(res,a);
        printf("%d\n",res);
        }       //for(i=0;i<l;i++)      printf("%d",a[i]);
        return 0;
}