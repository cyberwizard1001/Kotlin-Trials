#include<sys/ipc.h>
#include<sys/shm.h>
#include<sys/types.h>
#include<stdio.h>
#include<string.h>

int main()
{
    int retval, shmid;

    void *memory = NULL;

    char* p;

    //Initializing shared memory

    shmid = shmget((key_t)123456789,6,IPC_CREAT|0666);

    if(shmid<0)
    {
        printf("Key generation error\n");

        shmid = shmget((key_t)123456789,6,0666);
    }

    printf("Shared memory with id %d created\n",shmid);


    //attaching the shared memory
    memory = shmat(shmid,NULL,0);

    if(memory==NULL)
    {
        printf("Attachment failure\n");
        return 0;
    }

    p = (char*)memory;

    printf("Message is %s\n",p);

    //detach
    retval = shmdt(p);

    if(retval<0)
    {
        printf("Detached\n");

        return 0;
    }

    retval = shmctl(shmid,IPC_RMID,NULL);

    return 0;

    
}