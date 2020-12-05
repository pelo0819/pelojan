#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char* str = "hello";
    printf("str:%s, ptr:%p\n", str, str);
    int address = str;
    printf("%s.%08x.%08x.%08x.%08x.%08x\n", address);
    printf("\n");

    int ints[] ={1,4,6,8,2};
    printf("%d\n", argc);
    // printf("%d.%08x.%08x.%08x.%08x\n", ints[0]);
    // printf("%d%n", ints[0], ints[1]);

    int addr = str;
    // printf("sss%n\n", &addr);

    // char aa = 
    int a = atoi(argv[1]);
    printf("aa%d\n", a);

    printf("%d\n", addr);
    printf("%d\n", ints[0]);
    printf("%d\n", ints[1]);
    printf("%d\n", ints[2]);
    printf("%d\n", ints[3]);

    printf(argv[1]);

    return 0;
}
