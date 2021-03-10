#include<stdio.h>
#include<stdlib.h>
#include<sys/ipc.h>
#include<sys/types.h>
#include<sys/msg.h>

struct msgbuf {
    long mtype;
    int vote;
};

int main(void)
{
    struct msgbuf msg;

    int msgid;

    key_t key;

    if(key==ftok("polling_officer.c",'b')==-1)
    {
        perror("key");
        exit(1);
    }

    msgid=msgget(key,0644|IPC_CREAT);
    if(msgid==-1)
    {
        perror("msgid");
        exit(1);
    }

    printf("The queue ID is %d",msgid);
/*
    for(;;)
    {
        if(msgrcv(msgid,&msg,sizeof(msg),1,0)==-1)
        {
            perror("msgrcv");
            exit(1);
        }

        printf("%s\n",msg.mymsgtxt);
    }
*/

    printf("Enter vote (1/2/3): ");

    msg.mtype = 5;


    while(gets(msg.vote),!feof(stdin))
    {
        if(msgsnd(msgid,&msg,5,0)==-1)
        {
            perror("msgsnd");
            exit(1);
        }
    }


    if(msgctl(msgid,IPC_RMID,NULL)==-1)
    {
        perror("msgctl");
        exit(1);
    }

    return 0;

}

