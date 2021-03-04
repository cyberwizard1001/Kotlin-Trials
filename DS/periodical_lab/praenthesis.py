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
            #print("StackFullException")
            return
        else:
            self.t= self.t+1
            self.stack[self.t] = value
            return


    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if (self.size() == 0):
            #print("StackEmptyException")
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

    #@start-editable@

    def insert_parenthesis(self,pattern):

        open = 0
        
        for i in range (0,len(pattern)):

            while(open>=0):

                if(open==0 and i>0):
                    #print("if 3")
                    self.S.push("|")
                    
                if(pattern[i]=="("):
                    #print("if 1")
                    open+=1
                    self.S.push(pattern[i])
                    break

                if(pattern[i]==")"):
                    open-=1
                    self.S.push(pattern[i])
                    break

                if (open == self.S.max_stack_size): 
                    #print("SizeExceeded")
                    return 

        final = []
        while self.S.size()>0:
            final.append(self.S.pop())

        final.reverse()

        size = len(final)

        string = ""

        for x in final:
            #print(x)
            string = string + x

        string = string + "|"
        
        #logic call here.    
        self.logic(string)    

    def logic(self,string):
        #print(string)
        max = 0
        current = 0
        result = ""
        for x in string:
            if(x!="|"):
                result = result + x
                current+=1


            if(x=="|"):
                if(current>max):
                    max=current
                    current = 0
        print(str(max)+" "+result)            
        return			
			
    #@end-editable@   
        
        


def teststack():
    testcases = int(input())
    while testcases > 0:
        pattern = input()
        #Must use the stack ADT
        #@start-editable@

        stack = Parentheses(len(pattern)+10)
        stack.insert_parenthesis(pattern)
        testcases-=1

    return			
			
	    #@end-editable@


def main():
    teststack()


if __name__ == '__main__':
    main()