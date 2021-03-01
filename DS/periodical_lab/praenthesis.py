class MyStack():
    def __init__(self,size):
        self.stack = []
        # this is the stack container called 'stack'
        self.max_stack_size = size
        for i in range(self.max_stack_size):
            self.stack.append(None)
        # define the stack size 'max_stack_size' and initialize it
        self.t = -1
        #print(self.stack)

    # define the push operation which  pushes the value into the stack, must throw a stack full exception
    def push(self, value):
        if (self.size() == self.max_stack_size):
            print("StackFullException")
        else:
            self.t= self.t+1
            self.stack[self.t] = value
            return


    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if (self.size() == 0):
            print("StackEmptyException")
            return
        else:
            toret = self.stack[self.t]
            self.stack[self.t] = None
            self.t = self.t-1
            return toret


    # returns top element without removing it if the stack is not empty, else throws exception   
    def top(self):
        if (self.size() == 0):
            #print ("StackEmptyException")
            return
        else:
            return self.stack[self.t]


    # returns True if stack is empty   
    def isEmpty(self):
        return (self.t<0)

    # returns the number of elements currently in stack 
    def size(self):
        return (self.t+1)


    def printStack(self):
        if (self.isEmpty()):
            print("Empty")
        else:
            for i in range(self.max_stack_size):
                if self.stack[i]!=None:
                    print(self.stack[i],end=" ")
                    print(self.stack)
        return

class Parentheses():
    def __init__(self, stacksize):
        self.S = MyStack(stacksize)
        self.size = stacksize-2

    def insert_paranthesis(self,pattern):
        for i in range(0,len(pattern)):
            self.S.push(pattern[i])


    #@start-editable@
    def logic(self):
        
        pop_str = []
        i = 0
        count = 0
        j=0
        final_list = []
        
        for i in range(0,self.size):
            while(self.S.size()>0):
                print(i)
                pop_str.append(self.S.pop())
                i+=1

                if(pop_str[i]=='(' and count>0):
                    count+=1
                    final_list[j][i]='('

                if(pop_str[i]==')'):
                    count-=1
            
                    if(count>=0):
                        final_list[j][i]=')'
                

                if(count==0 and pop_str[i]=='('):
                    j+=1
                    count+=1
                    final_list[j][i]='('

                if(count<0):
                    break

            print(count,final_list)
            return


def teststack():
    testcases = int(input())
    while testcases > 0:
        pattern = input()
        #Must use the stack ADT
        #@start-editable@
        parentheses = Parentheses(len(pattern)+2)
        parentheses.insert_paranthesis(pattern)
        parentheses.logic()
			
	    #@end-editable@


def main():
    teststack()


if __name__ == '__main__':
    main()