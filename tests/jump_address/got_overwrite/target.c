#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int test()
{
    puts("test");
    return 0;
}

int main(int argc, char *argv[])
{
    char buf[100];
    printf("[+] buf = %p\n", buf);
    strncpy(buf, argv[1], sizeof(buf));
    printf(buf);
    putchar('\n');
    return 0;
}
