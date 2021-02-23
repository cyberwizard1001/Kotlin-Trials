//msgsend() - to send a message
//msgrcv() - to receive message
//msgctl() - delete to control 

#include<stdio.h>
#include<stdlib.h>
#include<sys/ipc.h>
#include<sys/types.h>
#include<sys/msg.h>

struct msgbuf
{
    long mtype;
    char mymsgtxt[200];
};

int main(void)
{
    struct msgbuf msg;

    int msgid;

    key_t key;
    //defined in msgsend
    //used by sender and reciever to confirm validity
    //is the message being recieved from the sender expected?

    key=ftok("message_send.c",'b');

    if(key==-1)
    {
        perror("key");
        exit(1);
    }

    //Generating queue 
    msgid=msgget(key,0644|IPC_CREAT);
    if(msgid==-1)
    {
        perror("msgid");
        exit(1);
    }

    printf("The msgid is %d",msgid);

    printf("Enter text: ");

    msg.mtype = 2;
    //can be any number as long as is not different in the 
    // two participating programs

    while(gets(msg.mymsgtxt),!feof(stdin))
    {
        int retval = msgsnd(msgid,&msg,sizeof(msg),0);
        if(retval==-1)
        {
            perror("msgsnd");
            exit(1);
        }
    }

    //Message created, collected from user
    //And sent to whoever wants it

    //time to delete the message queue

    if(msgctl(msgid,IPC_RMID,NULL)==-1)
    {
        perror("msgctl");
        exit(1);
    }

    return 0;

    //STEPS:
    //1) Create a key using a file which will 
    //correspond to the same key in the recieve file,
    // to make sure the processes are indeed the ones 
    //expected to communicate

    //2) The msgid is created by using the msgget() function
    //msgqueue is created here

    //3) If it has been created successfully,
    //get message from user and send it as it's being
    //typed out, using msgsend() with msgid, address and 
    //size of message as parameters. 


}

