#include<stdio.h>
#include<unistd.h>

int main(void)
{
    int pipefd[2];
    //this is to be passed to the pipe system call
    // to return file descriptor integers

    int ret;

    char buffer[20]; 
    //data buffer

    pipe(pipefd);
    //returns a read pipe and write 
    //pipe identifier, creates pipes

    ret = fork();
    //creating a child process
    //returns >0 for parent, 0 for child


    if(ret>0) //(parent process)
    {
        sleep(5);
        fflush(stdin);
        printf("Parent\n");

        //child writes data, parent is reading it

        read(pipefd[0],buffer,sizeof(buffer));
        //read data from buffer

        //display it
        write(1,buffer,sizeof(buffer));

    }

    if(ret==0)
    {
        fflush(stdin);

        printf("Child\n");

        write(pipefd[1],"DATA SENDING",13);
    }

    return 0;
}