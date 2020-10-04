#include<stdio.h>

void reverse(char* str)
{
	char* end = str;
	char tmp;
	if(str)
	{
		while(*end)
		{
			++end;
		}
	}
	--end;

	while(str < end)
	{
		tmp = *str;
		*str++ = *end;
		*end-- = tmp;
	}
	printf("%s \n",end);
}

int main( void )
{
	char name[10] = {'L','e','s','s','o','n','s','\0'};
	reverse(name);
	return 0;
}
