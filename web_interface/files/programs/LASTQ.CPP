#include<iostream.h>
#include<string.h>
#include<malloc.h>
typedef struct node{
	unsigned int info;
	struct node *next;
}node;
node *start=NULL,*end=NULL,*tempnode;
unsigned int returnvalue(char,unsigned int);
unsigned int getvalue(char*);
unsigned int prepare(char*);
void enqueue(unsigned int);
void popAll();
int main(){
	char *input;
	unsigned int numberinputs;
	cin>>numberinputs;
	for(unsigned int i=0;i<numberinputs;i++){
		cin>>input;
		enqueue(prepare(input));
	}
	popAll();
	return 0;
}
unsigned int prepare(char*S1){
	unsigned int len=strlen(S1);
	char *newS1=new char(len+1);
	strcpy(newS1,S1);
	//check if no star
	unsigned int count=0;
	for(unsigned int j=0;j<len;j++){
		if(newS1[j]=='*')
			count++;
	}
	if(count==0)
		return getvalue(S1);
	unsigned num=0;
	for(unsigned int i=0;i<len;i++){
		if(newS1[i]=='*'){
			newS1[i]='L';
			num+=prepare(newS1);
			newS1[i]='R';
			num+=prepare(newS1);
			newS1[i]='P';
			num+=prepare(newS1);
			break;
		}
	}
	return num;
}
unsigned int getvalue(char *S){
	unsigned int len=strlen(S);
	char *newS=new char(len+1);
	strcpy(newS,S);
	unsigned int num=1,temp=1;
	for(unsigned int i=0;i<len;i++){
		temp=returnvalue(newS[i],num);//is recursive and hence will add up
		if(temp==0)
			continue;
		else
			num=temp;
	}
	return num;
}
unsigned int returnvalue(char letter,unsigned int num){
	if(letter=='L')
		return 2*num;
	else
		if(letter=='R')
			return (2*num)+1;
		else
			return 0;
}
void enqueue(unsigned int a)
{
	tempnode=(node*)malloc(sizeof(node));
	tempnode->info=a;
	tempnode->next=NULL;
	if(start==NULL){
		end=start=tempnode;
	}
	else{
		end->next=tempnode;
		end=tempnode;
	}
}
void popAll()
{
	tempnode=start;
	while(tempnode!=NULL){
		cout<<tempnode->info<<endl;
		tempnode=tempnode->next;
	}
}