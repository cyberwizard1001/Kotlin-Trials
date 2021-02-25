#include<stdio.h>
#include<string.h>

struct rainfall{
    char date[10];
    int rainfall;
}var;

int rainfall_month[12];

void rainfall_calc()
{
    int compare = (int)var.date[3];
    if(compare==48)
    {
        switch((int)var.date[4])
        {
            case 49:
                rainfall_month[0]+=var.rainfall; 
                break;

            case 50:
                rainfall_month[1]+=var.rainfall; 
                break;

            case 51:
                rainfall_month[2]+=var.rainfall; 
                break;

            case 52:
                rainfall_month[3]+=var.rainfall; 
                break;

            case 53:
                rainfall_month[4]+=var.rainfall; 
                break;

            case 54:
                rainfall_month[5]+=var.rainfall; 
                break;

            case 55:
                rainfall_month[6]+=var.rainfall; 
                break;

            case 56:
                rainfall_month[7]+=var.rainfall;
                break;

            case 57:
                rainfall_month[8]+=var.rainfall;
                break;

        }

        
    }

    compare = (int)var.date[3];
    if(compare==49)
    {
        if((int)var.date[4]==48)
        {
            rainfall_month[9]+=var.rainfall; 
        }

        if((int)var.date[4]==49)
        {
            rainfall_month[10]+=var.rainfall;
        }

        if((int)var.date[4]==50)
        {
            rainfall_month[11]+=var.rainfall;
        }
    }
}

int main()
{
    int num;
    scanf("%d",&num);

    for(int i=0;i<12;i++)
    {
        rainfall_month[i]=0;
    }

    for(int i=0;i<num;i++)
    {
        scanf("%s",var.date);
        scanf("%d",&var.rainfall);

        rainfall_calc();
    }

    for(int j=0;j<12;j++)
    {
        switch(j)
    {
        case 0:
            if(rainfall_month[j]>0)
                printf("Jan %d\n",rainfall_month[0]);

            break;

        case 1:
            if(rainfall_month[j]>0)
                printf("Feb %d\n",rainfall_month[1]);

            break;

        case 2:
                if(rainfall_month[j]>0)
                printf("Mar %d\n",rainfall_month[2]);

                break;

        case 3:
                if(rainfall_month[j]>0)
                printf("Apr %d\n",rainfall_month[3]);

                break;

        case 4:
            if(rainfall_month[j]>0)
                printf("May %d\n",rainfall_month[4]);

            break;

        case 5:
            if(rainfall_month[j]>0)
                printf("Jun %d\n",rainfall_month[5]);

            break;

        case 6:
            if(rainfall_month[j]>0)
                printf("Jul %d\n",rainfall_month[6]);

            break;

        case 7:
            if(rainfall_month[j]>0)
                printf("Aug %d\n",rainfall_month[7]);

            break;

        case 8:
            if(rainfall_month[j]>0)
                printf("Sep %d\n",rainfall_month[8]);

            break;

        case 9:
            if(rainfall_month[j]>0)
                printf("Oct %d\n",rainfall_month[9]);

            break;

        case 10:
            if(rainfall_month[j]>0)
                printf("Nov %d\n",rainfall_month[10]);

            break;

        case 11:
            if(rainfall_month[j]>0)
                printf("Dec %d\n",rainfall_month[11]);

            break;
        }
    
    }

    return 0;
}