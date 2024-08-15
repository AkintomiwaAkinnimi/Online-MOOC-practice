#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i quarters + %i dimes + %i nickels + %i pennies\n", quarters, dimes, nickels, pennies);
}

int get_cents(void)
{
    int a;
    do
    {
        a = get_int("Number of cents: ");
        if (a < 1)
        {
            printf("Enter number of cents > 1\n");
        }

    }
    while (a < 1);
    return a;
}

int calculate_quarters(int a)
{
    int quarters = 0;
    while (a >= 25)
    {
         a = a - 25;
        quarters++;
    }
    return quarters;
}

int calculate_dimes(int a)
{
   int dimes = 0;
   while (a >= 10)
   {
    a = a - 10;
    dimes++;
   }
    return dimes;
}

int calculate_nickels(int a)
{
    int nickels = 0;
    while (a >= 5)
    {
        a = a - 5;
        nickels++;
    }
    return nickels;
}

int calculate_pennies(int a)
{
    int pennies = 0;
    while (a >= 1)
    {
        a = a - 1;
        pennies++;
    }
    return pennies;
}
