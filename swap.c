#include <cs50.h>
#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 4;

    printf("x is %i and y is %i\n", x, y);
    swap (&x, &y);
    printf("x is %i and y is %i\n", x, y);
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
