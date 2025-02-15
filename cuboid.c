#include<stdio.h>
void main()
//taking dots as vertices for stacked plains
{
    int height, width, length, row, column, space, increment = 0, i, total, height_copy;

    printf("Enter desired length: ");
    scanf("%d",&length);
    printf("Enter desired width: ");
    scanf("%d",&width);
    printf("Enter desired height: ");
    scanf("%d",&height);

    total = (2*length) + width;

//TOP HALF OF CUBOID
    for(row = 0 ; row < (width + height) && (width - increment) > 0 ; row++) {
        printf("\n");

        //printing starting spaces
        for(space = (width - increment) ; space > 0 ; space--) {
            printf(" ");
        }
        increment++;

        //printing top face
        for(i = 0 ; i < length ; i++) {
            printf("o ");
        }

        //printing side face in top half
        for(i = 0 ; i < (total - (2*length) - (width - increment)) && i <= height ; i++) {
            printf("o");
        }
    }

    height_copy = height;

//BOTTOM HALF OF CUBOID
    for( ; row <= (width + height) ; row++) {
        printf("\n");
        height_copy--;
       
        //printing front face
        for(i = 0 ; i < length ; i++) {
            printf(". ");
        }

        //printing side face in bottom half
        for(i = 0 ; i <= (total) - (2*length) && i <= height_copy + 1; i++) {
            printf("o");
        }
    }

    printf("\n\n");
}