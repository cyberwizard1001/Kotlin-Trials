#include <stdio.h> 
#include <stdlib.h> 
#include <pthread.h> 
#include <unistd.h> 


void *SampleThread1(void *vargp) 
{
    int i = 0; 
    printf("SampleThread(1) is running ... \n"); 
    for(i = 0; i < 3; i++) { 
        sleep(1); 
        printf("timer running inside SampleThread(1) = %d\n", i); 
    } 

    printf("SampleThread(1) is exiting ... \n"); 
    return NULL; 
} 

void *SampleThread2(void *vargp) 
{ 

    int i = 0;
    printf("SampleThread(2) is running ... \n"); 
    for(i = 0; i < 5; i++) { 
        sleep(1);
        printf("timer running inside SampleThread(2) = %d\n", i); 
    } 

    printf("SampleThread(2) is exiting ... \n"); 
    return NULL; 

}

int main() 
{ 

    int i = 0; 
    pthread_t tid1, tid2; 
    pthread_create(&tid1, NULL, SampleThread1, NULL); 
    pthread_create(&tid2, NULL, SampleThread2, NULL); 

    printf("timer outside Thread is ended ..\n"); 
    pthread_join(tid1, NULL); 
    pthread_join(tid2, NULL); 
    
    exit(0); 

} 