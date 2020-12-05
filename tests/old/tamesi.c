#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char* str = "AAA";
    printf("str:%s, ptr:%p\n", str, str);
    int address = str;
    printf("%s.%08x.%08x.%08x.%08x.%08x\n", address);
    printf("%s.%5$08x\n", address);
    printf("\n");

    int ints[] ={1,4,6,8,2};
    int addrInts0 = ints[0];
    printf("%p\n", ints);

    int a = atoi(argv[1]);
    printf("aa%d\n", a);
    printf(argv[1]);

    return 0;
}
