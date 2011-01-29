#include<stdio.h>
char b[300];
int gcd(int,int);
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int a,i=0;
        //b=(char *)malloc(sizeof(char)*300);
        scanf("%d %s",&a,b);
        int len=strlen(b);
        int c=1;
        int pow=len-1;
        int res=0;
        if(a==0)
        printf("%s\n",b);
        else if(len==1 && *(b+0)=='0')
        printf("%d\n",a);
        else{
        for(i=0;i<len;i++)
        {
            res=(res+(c%a)*(*(b+len-1-i)-'0'))%a;
            c=(c*10)%a;           
        }
        printf("%d\n",gcd(a,res%a));
        } 
        //free(b);                
    }  
      
      return(0);
}
int gcd(int a,int b)
{
    if(b==0)
    return(a);
    else
    return(gcd(b,a%b));
}
    
