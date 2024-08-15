#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_grid(int get_size);

int main(void)
{
    // Get size of bricks
    int n = get_size();

    // Print size of bricks
    print_grid(n);
}






int get_size(void)
{
    int n;
    do
    {
        n = get_int("Size ");
        if (n <= 1)
        {
            printf("Enter size > 1\n");
        }
    }
    while (n <= 1);
    return n;
}

void print_grid(int n)
{
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < n; c++)
        {
            printf("#");
        }
        printf("\n");
    }

}
