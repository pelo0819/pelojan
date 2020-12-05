#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // char* str = "AAA";
    // printf("str:%s, ptr:%p\n", str, str);
    // int address = str;
    // printf("%s.%08x.%08x.%08x.%08x.%08x\n", address);
    // printf("%s.%5$08x\n", address);
    // printf("\n");

    // int ints[] ={1,4,6,8,2};
    // int addrInts0 = ints[0];
    // printf("ints pointer:%p\n", ints);
    
    // printf("ints");
    // printf(ints);
    // printf('\n');
    
    // int a = atoi(argv[1]);
    // printf("aa%d\n", a);
    // printf(argv[1]);

    int *a;
    int b = 2;
    a = &b;
    printf("[*] BEFORE a:%d, a_ptr:%p\n" , *a, a);

    char buf[100];
    strncpy(buf, argv[1], 100);
    printf(buf);
    printf("\n");

    printf("[*] AFTER  a:%d, a_ptr:%p\n" , *a, a);

    return 0;
}
