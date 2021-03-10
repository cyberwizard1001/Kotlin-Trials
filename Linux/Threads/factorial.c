#include <stdio.h>
#include <pthread.h>



void* fact(void* p){
  
  int prod = 1;
  printf("Value of argument passed: %d\n",*(int*)p);
  for(int i=1;i<=*(int*)p;i++)
  {
      prod*=i;
  }

  pthread_exit(prod);
}

int main(void){
  // Declare variable for thread's ID:
  pthread_t id;

  int input = 0;
  printf("Enter number to find factorial: ");
  scanf("%d",&input);
  pthread_create(&id, NULL, fact, &input);
    
  int* retval;

  
  pthread_join(id, (void**)&retval);
  printf("\nFactorial of %d: %d",input,retval);

  return 0;
}