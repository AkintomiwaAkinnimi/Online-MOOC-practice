#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[4];

    people[0].name = "Tomiwa";
    people[0].number = "08102158459";

    people[1].name = "Funmi";
    people[1].number = "08124456046";

    people[2].name = "Atoyebi";
    people[2].number = "08023129366";

    people[3].name = "Akinnimi";
    people[3].number = "08023655789";

    string name = get_string("Enter name: ");
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
            printf("%s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
