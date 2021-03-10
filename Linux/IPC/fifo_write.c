#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<fcntl.h>
#include<unistd.h>
//refer manpage of fifo to understand what headers to use



int main()
{
    int fd, retval;
    char buffer[9] = "TESTDATA";

    fflush(stdin);

    retval = mkfifo("/tmp/myfifo",0666);
    //create fifo -> in directory tmp/myfifo

    fd = open("/tmp/myfifo",O_WRONLY);
    //open the fifo, which is a file and hence returns
    // a file descripter as integer, which is then used 
    // to then write to the file.2

    write (fd,buffer,sizeof(buffer));
    //write to buffer
    
    close(fd);

    return 0;
}