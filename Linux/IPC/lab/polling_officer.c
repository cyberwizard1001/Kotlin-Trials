#include <stdio.h> 
#include <sys/ipc.h> 
#include <sys/msg.h> 
#include<string.h>
  
// structure for message queue 
struct mesg_buffer { 
    long mesg_type; 
    int mesg_text; 
} message; 
  
int main() 
{ 
    key_t key; 
    int msgid; 

    int cnt1 = 0,cnt2 = 0,cnt3 = 0;
  
    
    key = 1234; 
  
    
    msgid = msgget(key, 0666 | IPC_CREAT); 
  
    for(int i=0;i<5;i++)
    {
        msgrcv(msgid, &message, sizeof(message), 1, 0);
        printf("%d Vote received is : %d \n",i+1,message.mesg_text); 


        if(message.mesg_text==1)
        {
            cnt1++;
        }

        else if(message.mesg_text==2)
        {
            cnt2++;
        }

        else if(message.mesg_text==3)
        {
            cnt3++;
        }

        else
        {
            printf("Invalid vote\n");
        }

    }
   
    printf("Final tally:\n");
    printf("Contestant 1: %d\n",cnt1);
    printf("Contestant 2: %d\n",cnt2);
    printf("Contestant 3: %d\n",cnt3);

    msgctl(msgid, IPC_RMID, NULL); 
  
    return 0; 
} 