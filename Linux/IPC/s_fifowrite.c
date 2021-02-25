#include<stdio.h>
#include<unistd.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<fcntl.h>
int main()
{
int fd, retval;
char buffer[10];
printf("\nEnter the data");

scanf("%[^\n]",buffer);
    fflush(stdin); 
retval=mkfifo("/tmp/myfifo",0666);
fd =open("/tmp/myfifo",O_WRONLY);
write(fd,buffer,sizeof(buffer));
close(fd);

return 0;
}