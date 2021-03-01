#include <pthread.h> 
#include <stdio.h> 
#include <stdlib.h> 

 

struct student{ 

    char name[100]; 
    char roll_no[10];
    char year[3];
}Student; 

int marks[5];

void *get_details(void *input) { 
    
    printf("Enter student name: ");
    scanf("%s", Student.name); 
    printf("Enter roll number: ");
    scanf("%s", Student.roll_no); 
    printf("Enter grade/year:" );
    scanf("%s", Student.year);

} 

void *get_marks(void *input)
{
    for(int i=0;i<5;i++)
    {
        printf("Mark %d: ",i+1);
        scanf("%d",&marks[i]);
    }
}

 

int main(void) { 


    pthread_t tid, tid_2; 

    pthread_create(&tid, NULL, get_details, NULL); 
    pthread_join(tid, NULL); 

    pthread_create(&tid_2, NULL, get_marks, NULL); 
    pthread_join(tid_2,NULL);

    int sum = 0;
    char final[2];

    for(int i=0;i<5;i++)
    {
        sum+=marks[i];
    }

    sum = sum/5;
    
    

    printf("Student details: \n");
    printf("Name: %s\n",Student.name);
    printf("Roll number: %s\n",Student.roll_no);
    printf("Grade/Year: %s",Student.year);

    printf("Average: %d\n",sum);

    if(sum<=100 && sum>90)
    {
        printf("Final grade: O");
    }

    else if(sum<=90 && sum>70)
    {
        printf("Final grade: A");
    }

    else if(sum<=70 && sum>60)
    {
        printf("Final grade: B");
    }

    else if(sum<=60 && sum>50)
    {
        printf("Final grade: C");
    }

    else if(sum<=50 && sum>40)
    {
        printf("Final grade: D");
    }

    else
    {
    
        printf("Final grade: F");
    }

    


return 0; 

} 
