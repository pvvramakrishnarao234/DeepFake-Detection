#include<iostream>

using namespace std;

int main()
{
  int number,head=2,tail=3,i,symbol,count=0;
  cin>>number;
  int myarray[number]={1,2,2};
  while(tail!=number)
    {
      symbol=myarray[tail-1]==2?1:2;
      if(myarray[head]==2)
	{
   	  myarray[tail++]=symbol;
	  myarray[tail++]=symbol;
	}
      else
	{
	  myarray[tail++]=symbol;
	}
      head++;
    }
  for(auto e:myarray)
    {
      if(e==2)
	count++;
	}
  cout<<count;
}
