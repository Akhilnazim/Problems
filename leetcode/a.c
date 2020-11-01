#include <stdio.h>

int a1(int x);
int a2(int y);

void main()
{
  int n;
  scanf("%d",&n);
  if(n%2==0)
  a1(n/2);
  else
    a2(n/2+1);
}

int a1(int x)
{
int s=0;
for(int i=0;i<x-1;i++)
{
s=s+6;
}
printf("%d",s);
}

int a2(int x)
{
int s=0;
for(int i=0;i<x-1;i++)
{
s=s+7;
}
printf("%d",s);
}