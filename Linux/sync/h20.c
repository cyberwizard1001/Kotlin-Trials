#include<pthread.h>
#include<semaphore.h>
#include<stdio.h>
#include<stdlib.h>

//variables - count variables 
int n_w_oxy = 0;
int n_w_hydro = 0;
int n_oxy = 0;
int n_hydro = 0;
int n_water = 0;


//threads
pthread_t thread_oxy;
pthread_t thread_hydro;

//variables - mutex and semaphore
pthread_mutex_t lock; //mutex
sem_t sem_oxy;
sem_t sem_hydro;


void *Hydrogen(void* param)
{
    pthread_mutex_lock(&lock);

    //producing a water molecule 
    while(n_w_hydro==0)
    {
        if(n_hydro>=2 && n_oxy>=1)
        {
            n_hydro-=2; n_w_hydro+=2;
            n_oxy-=1; n_w_oxy+=1;
            n_water+=1;
            printf("Water moluecule produced. Number: %d\n",n_water);
            sem_post(&sem_oxy);
            sem_post(&sem_hydro);
        }
        //if enough molecules are not available, wait
        else{
            sem_wait(&sem_hydro);
        }
    }
    n_w_hydro--;
    pthread_mutex_unlock(&lock);
}

void *Oxygen(void* param)
{
    pthread_mutex_lock(&lock);
    n_oxy++;

    //producing a water molecule 
    while(n_w_oxy==0)
    {   
        if(n_hydro>=2 && n_oxy>=1)
        {
            n_hydro-=2; n_w_hydro+=2;
            n_oxy-=1; n_w_oxy+=1;
            n_water+=1;
            printf("Water moluecule produced. Number: %d\n",n_water);

            sem_post(&sem_oxy);
            sem_post(&sem_hydro);
        }
        //if enough molecules are not available, wait
        else{
            sem_wait(&sem_oxy);
        }
    }
    n_w_oxy--;
    pthread_mutex_unlock(&lock);
}


int main()
{
    n_oxy = 2;
    n_hydro = 4;

    sem_init(&sem_oxy,0,1);  //sem,pshared,value 
    sem_init(&sem_hydro,0,1);
    for(int i=0;i<100000;i++)
    {
        if(i%3!=0)
        {
            pthread_create(&thread_hydro,NULL,Hydrogen,NULL);
        }

        else
        {
            pthread_create(&thread_oxy,NULL,Oxygen,NULL);
        }

    }

    
        pthread_join(thread_oxy,NULL);			//Join Oxygen thread.
        pthread_join(thread_hydro,NULL);			//Join Hydrogen thread.

    return 0;
}
