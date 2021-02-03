class DLList:
    class node:
        def __init__(self,data):
            self.element = data
            self.next = None
            self.prev = None
           
          
    def __init__(self):
        self.head = self.node(None)
        self.tail = self.head
        self.sz = 0

    def getHead(self):
        #@start-editable@

        return self.head.element
			
	    #@end-editable@
        return
    
        def getLastNode(self):
        #@start-editable@

            return self.tail.element
            
        #@end-editable@
        return
     
    def insertLast(self,u):
        #@start-editable@

		#create node with element u
        nnode = self.node(u)

        #if list is empty, insert said node at head. It'll 
        #automatically become tail in the end
        
        if(self.size()==0):
            self.tail=self.head
            self.head.element = u

        #set existing tail's next to nnode, 
        #set nnode as tail
        
        nnode.next=None
        self.tail.next = nnode
        nnode.prev = self.tail
        self.tail=nnode
        self.sz+=1

			
	    #@end-editable@
        return

    def insertFirst(self,u):
        #@start-editable@

		#creating a new node with given data
        nnode = self.node(u)

        
        #making head's value as u 
        if(self.isEmpty()):
            self.head.element=u
            print(self.sz)

        else:
            nnode.next = self.head
            self.head.prev = nnode
            self.head = nnode
        
        self.sz+=1	
			
	    #@end-editable@
        return
        
         
    #insert a node with value u after the node containing value v
    # error message: Node to insert after not found
    def insertAfter(self,u,v):
        #@start-editable@

        nnode = self.node(u)

        tnode = self.findNode(v)

        if(tnode!=None):
            tnode.next=nnode
            nnode.prev=tnode
            nnode.next=tnode.next
            tnode.next.prev=nnode
            self.sz+=1
            
        else:
            print("Node to insert after not found")
            
        #@end-editable@
        return


    #insert a node with value u before the node containing value v
    # error message: Node to insert before not found
    def insertBefore(self,u,v):
        #@start-editable@

        nnode = self.node(u)

        tnode = self.findNode(v)

        if(tnode!=None):
            #set tnode to point to previous node
            tnode=tnode.prev

            #procedure to insert node after tnode (check)
            tnode.next=nnode
            nnode.prev=tnode
            nnode.next=tnode.next
            tnode.next.prev=nnode
            self.sz+=1
            
        else:
            print("Node to insert before not found")
            
        #@end-editable@
        return

    def deleteFirst(self):
        #@start-editable@

		#check if it's empty
        if self.size()==0:
            return

        #deleting head

        #Set prev of second element to None
        self.head.next.prev=None

        #Set pointer to existing head to delete later
        tnode = self.head

        #make second node as head node
        self.head = self.head.next

        #make head node's prev point to None
        self.head.prev=None

        #delete tnode thereby removing old head
        del tnode
        self.sz-=1
			
	    #@end-editable@
        return

    def deleteLast(self):
        #@start-editable@

		#check if it's empty
        if self.size()==0:
            return

        #deleting tail

        #make a copy of original tail for deletion
        tnode = self.tail

        #make tail's prev node tail
        self.tail = self.tail.prev

        #set tail's next as None
        self.tail.next=None

        #set ex-tail's prev as None (to remove connection to current tail)
        tnode.prev = None

        #delete tnode, and hence old tail
        del tnode
        self.sz-=1
	
			
	    #@end-editable@
        return  

    #delete the node after the node containting value u
    # error message: Node to delete after not found
    def deleteAfter(self,u):
        #@start-editable@

        tnode = self.findNode(u)

        if(tnode!=None):
            #setting tnode as next node (ie to be deleted node)
            tnode = tnode.next

            #making prev node point to next node
            tnode.pre.next=tnode.next

            #making next node's prev point to prev node
            tnode.next.prev = tnode.prev

            #deleting node 
            del tnode
            self.sz-=1

        else:  
            print("Node to delete after not found")
            
        #@end-editable@
        return

    #delete the node before the node containting value u
    # error message: Node to delete before not found
        def deleteBefore(self,u):
        #@start-editable@

            tnode = findNode(u)

        if(tnode!=None):
            #setting node to be deleted as tnode
            tnode = tnode.prev

            #making prev node point to next node
            tnode.pre.next=tnode.next

            #making next node's prev point to prev node
            tnode.next.prev = tnode.prev

            #deleting node 
            del tnode
            self.sz-=1

        else: #INSERT ERROR
            print("Node to delete before not found")

            
        #@end-editable@
        return

        def findNode(self, val):
        #@start-editable@

            tnode = self.head

        #traverse
        flag = False
        while(tnode.next!=None and not flag):
            
            if(tnode.element!=val):
                tnode=tnode.next

            else: flag=True

        #if element exists, return it
        if(flag):
            return tnode
            
        else:  
            return
            
        #@end-editable@
        return

        #swap the nodes containing u and v
        def swap(self,u,v):
        #@start-editable@
            
        #@end-editable@
            return
 
    def isEmpty(self):
        #@start-editable@
			
	    #@end-editable@
        return (self.sz==0)

    def size(self):
        #@start-editable@
			
	    #@end-editable@
        return self.sz

    def printList(self):
        if (self.isEmpty()):
            print ("Linked List Empty Exception")
        else:
            tnode = self.head
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.next
            print(" ")
            tnode = self.tail
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.prev
            print(" ")
        return
    
def testDLL():
    dll = DLList()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(dll.size())
        elif(operation[0]=="I"):
            print(dll.isEmpty())
        elif(operation[0]=="IF"):
            dll.insertFirst(int(operation[1]))
            dll.printList()
        elif(operation[0]=="IL"):
            dll.insertLast(int(operation[1]))
            dll.printList()
        elif(operation[0]=="DF"):
            dll.deleteFirst()
            dll.printList()
        elif(operation[0]=="DL"):
            dll.deleteLast()
            dll.printList()
        elif(operation[0]=="IA"):
            dll.insertAfter(int(operation[1]),int(operation[2]))
            dll.printList()
        elif(operation[0]=="IB"):
            dll.insertBefore(int(operation[1]),int(operation[2]))
            dll.printList()
        elif(operation[0]=="DA"):
            dll.deleteAfter(int(operation[1]))
            dll.printList()
        elif(operation[0]=="DB"):
            dll.deleteBefore(int(operation[1]))
            dll.printList()   
        elif(operation[0]=="F"):
            print(dll.getHead().element)
        elif(operation[0]=='L'):
            print(dll.getLastNode().element)
        elif(operation[0]=='FIND'):
            temp = dll.findNode(int(operation[1]))
            if (temp!=None):
                print(temp.element)
            else:
                print("NULL")
        elif(operation[0]=='SW'):
            dll.swap(int(operation[1]),int(operation[2]))
            dll.printList()
        inputs-=1


def main():
    testDLL()

if __name__ == '__main__':
    main()