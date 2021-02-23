#include <stdio.h> 
#include <sys/ipc.h> 
#include <sys/msg.h> 

  
// structure for message queue 
struct mesg_buffer { 
    long mesg_type; 
    int mesg_text;
};  
  
int main() 
{ 
    struct mesg_buffer message;
    key_t key; 
    int msgid; 
  
    
    key = 1234; 
  
    
    msgid = msgget(key, 0666 | IPC_CREAT); 
    message.mesg_type = 1; 
  
    printf("Enter vote: "); 
    scanf("%d",&message.mesg_text);
  
    
    msgsnd(msgid, &message, sizeof(message), 0); 
  
    
    printf("Vote: %d \n", message.mesg_text); 
  
    return 0; 
} 