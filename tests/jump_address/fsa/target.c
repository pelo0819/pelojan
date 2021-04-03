#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char buf[100];
    char *secret;
    FILE *fp;

    secret = malloc(2000);
    printf("[+] secret = %p\n", secret);
    printf("[+] buf = %p\n", buf);

    fp = fopen("./resources/fsc_test.txt", "r");
    fread(secret, 1, 2000, fp);
    fclose(fp);
    printf("length = %d\n", strlen(secret));

    strncpy(buf, argv[1], sizeof(buf));
    printf(buf);
    printf("\n");

    free(secret);
    return 0;
}
