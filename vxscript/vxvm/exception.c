#include <stdio.h>
#include <stdlib.h>

void throw(char *name, char *info) {
	printf("ERR: %s appeaered beacuse:\r\n\t%s\r\n",name,info);
	exit(-1);
}
