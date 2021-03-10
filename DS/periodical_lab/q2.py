class Node:
    def __init__(self, key, next=None):
        self.data = key
        self.next = next
 
 
class Queue:
 
    def __init__(self):
        self.fnt = None
        self.rear = None
        self.sz = 0
        
    def enqueue(self, x):  
        temp = Node(x)
        if self.sz==0: 
           self.fnt = temp
           self.rear = temp 
           self.sz=self.sz+1
           return
        else:
           self.rear.next = temp 
           self.rear = temp 
           self.sz=self.sz+1
           return
        return

    def dequeue(self):  
        if self.sz==0: 
           print("Queue Empty Exception")
           return
        else:
           temp = self.fnt 
           self.fnt = temp.next
           self.sz=self.sz-1
           return temp
        return

    def isEmpty(self):
        if self.sz==0:
           return True
        else:
           return False
        return
     
    def front(self):
        if self.sz==0:
           print("Queue Empty Exception")
           return
        else:
           return self.fnt
        return
    
    def size(self):
        return self.sz
    

    def printQueue(self):
        if self.isEmpty():
            print("Queue Empty Exception")
        else:
            tnode = self.fnt
            while tnode!=None:
                print(tnode.data,end=" ")
                tnode = tnode.next
            print("")
        return

class myVideoBuffer:
    def __init__(self):
        self.myBuffer = Queue()
        return 

    def createBuffer(self,element):
        #@start-editable@

        if self.myBuffer.isEmpty():
            self.myBuffer.enqueue(element)
            return 

        self.myBuffer.enqueue(element)

        if(self.myBuffer.size()==1):
            if(element>self.myBuffer.front().data):
                self.myBuffer.enqueue(self.myBuffer.dequeue())

        while(self.myBuffer.front().data<element):
            self.myBuffer.enqueue(self.myBuffer.dequeue)
        
        self.myBuffer.enqueue(element)
        
        
        #@end-editable@
        return

    def display(self):
        #@start-editable@

        self.myBuffer.dequeue()
        
        #@end-editable@
        return
    
    # for any functions you may wish to write    
    #@start-editable@

    
    
    
    #@end-editable@


    def startStreaming(self,K):
        #@start-editable@

        n = 1
        while not self.myBuffer.size()==0:
            if n%K!=0:
                self.display()
            else:
                print("\n")
        
        
        #@end-editable@
        return
    
    
        

            

        

 

# Driver code.---------------------------------------------

def testBuffer():
    Bu = myVideoBuffer()
    inputs=int(input())
    K =int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="I"):
            Bu.createBuffer(int(operation[1]))
        elif(operation[0]=="S"):
            print("Stream Start")
            Bu.startStreaming(K)
            print("Stream End")
        elif(operation[0]=="P"):
            Bu.display()
        else:
            print("INVALID INPUT")
        inputs-=1

def main():
    testBuffer()

if __name__ == '__main__':
    main()