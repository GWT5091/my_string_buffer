#include<stdio.h>

void reverse(char* str)
{
	printf("%s\n", str);
	int count = 0;
	while(str[count] != '\0')
	{
		count++;
	}
	char rename[count+1];
	rename[count]= '\0';
	int i = 0;
	for(;count>0;count--)
	{
		rename[i] = str[count-1];
		i++;
	}
	printf("%s\n",rename);
}

int main( void )
{
	char name[10] = {'L','e','s','s','o','n','s','\0'};
	reverse(name);
	return 0;
}
