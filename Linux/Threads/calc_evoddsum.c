#include <stdio.h> 
#include <stdlib.h> 
#include <pthread.h> 

int size = 0;
int ev_sum = 0;
 
void *evensumcalc(void *array) 

{ 
    
    int *Array = (int *)array;

    for(int i=0;i<size;i++)
    {
        if(Array[i]%2==0)
        {
            ev_sum+=Array[i];
        }
    }
    
    return ev_sum; 

} 

 

int main() 

{ 
    pthread_t tid; 
    printf("Enter array size: ");
    scanf("%d",&size);

    int array[size];
    int od_sum = 0;

    printf("Enter array elements: \n");

    for(int i=0;i<size;i++)
    {
        printf("array[%d]: ",i);
        scanf("%d",&array[i]);
    }

    pthread_create(&tid, NULL, evensumcalc, array); 

    for(int i=0;i<size;i++)
    {
        if(array[i]%2==1)
        {
            od_sum+=array[i];
        }
    }

    int* ev_sum;
    pthread_join(tid,&ev_sum); 

    printf("Even sum (from thread: ): %d\n",ev_sum);
    printf("Odd sum (from main): %d\n",od_sum);

    exit(0); 

} 