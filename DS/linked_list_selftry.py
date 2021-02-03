class SLList:

    class node:
        def __init__(self,data):
            self.element = data
            self.next = None
        
    def __init__(self):
        self.head = self.node(None)
        self.sz = 0
          
          
    def insertLast(self,data):
        #@start-editable@

        nnode = self.node(data)

        if self.isEmpty():
            self.head = nnode
            
        else:
            tnode = self.head

            while tnode.next!=None:
                tnode = tnode.next
            
            tnode.next = nnode
            self.sz+=1
        
        
        
        #@end-editable@
        return

    def insertFirst(self,data):
        #@start-editable@

        nnode = self.node(data)

        if self.isEmpty():
            self.head = nnode

        else:
            nnode.next = self.head
            self.head = nnode
            self.sz+=1
        
        #@end-editable@
        return
     
    def deleteFirst(self):

        #@start-editable@

        if self.size() ==0:
            print("ListEmptyException")

        elif self.size() == 1:
            self.head.element = None
            self.sz-=1
            
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.sz-=1

        
        
        #@end-editable@
        return

    def deleteLast(self):
        #@start-editable@

        if self.size() == 0:
            print("ListEmptyException")
            
        elif self.size()==1:
            self.head.element = None
            self.sz=-1
            
        else:
            curnode = self.head
            while curnode.next.next!=None:
                curnode = curnode.next
                
            curnode.next = None
            self.sz-=1
        
        
        #@end-editable@
        return

          
    def printList(self):
        if (self.isEmpty()):
            print ("List Empty")
        else:
            tnode = self.head
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.next
            print("null")
        return
     
    def findNode(self, val):
        #@start-editable@

        if self.size()==0:
            print("ListEmptyException") 
            
        else:
            curnode = self.head
		
            while curnode.next != None:
                if curnode.element == val:
                    return curnode.element
                
                curnode = curnode.next
        
        #@end-editable@
        return None
        
    def getHead(self):
        #@start-editable@

         return self.head.element
        
        #@end-editable@
     
    def isEmpty(self):
        #@start-editable@

        return(self.sz==0)
        
        #@end-editable@

    def size(self):
        #@start-editable@

        return self.sz
        
        #@end-editable@
		  
    def getLastNode(self):
        #@start-editable@

        curnode = self.head
        while curnode.next!=None:
            curnode = curnode.next
            
        return curnode
        
        #@end-editable@
		  
    def delKth(self, k):
          
        #@start-editable@

        if self.size()==0:
            print("ListEmptyException") 
        
        if k == 0:
            curnode = self.head
            self.head = curnode.next
            curnode = None
            self.sz-=1
            return
        
        else:
            curnode = self.head
            count = 0

            while count<k-1:
                curnode = curnode.next
                count+=1
            
            curnode.next = curnode.next.next
            self.sz-=1
        return 
        
        #@end-editable@
     
    def swapAdj(self):
          
        #@start-editable@

        
        
        
        #@end-editable@
     
def testSLL():
    sll = SLList()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(sll.size())
        elif(operation[0]=="I"):
            print(sll.isEmpty())
        elif(operation[0]=="AF"):
            sll.insertFirst(int(operation[1]))
            sll.printList()
        elif(operation[0]=="AL"):
            sll.insertLast(int(operation[1]))
            sll.printList()
        elif(operation[0]=="RF"):
            sll.deleteFirst()
            sll.printList()
        elif(operation[0]=="RL"):
            sll.deleteLast()
            sll.printList()
        elif(operation[0]=="F"):
            print(sll.getHead())
        elif(operation[0]=='L'):
            print(sll.getLastNode())
        elif(operation[0]=='FIND'):
            print(sll.findNode(int(operation[1])))
        elif(operation[0]=='DK'):
            sll.delKth(int(operation[1]))
            sll.printList()
        elif(operation[0]=='SA'):
            sll.swapAdj()
            sll.printList()
        inputs-=1


def main():
    testSLL()

if __name__ == '__main__':
    main()