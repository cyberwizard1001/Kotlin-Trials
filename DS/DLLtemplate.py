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

        return self.head
			
	    #@end-editable@
        
    
    def getLastNode(self):
        #@start-editable@

        return self.tail	
			
	    #@end-editable@
        
     
    def insertLast(self,u):
        #@start-editable@

		#create node with element u
        nnode = self.node(u)

        #if list is empty, insert said node at head. It'll 
        #automatically become tail in the end
        if(self.size()==0):
            self.tail=self.head = nnode
            self.sz+=1

        #set existing tail's next to nnode, 
        #set nnode as tail
        else:
            nnode.next=None
            self.tail.next = nnode
            nnode.prev = self.tail
            self.tail=nnode
            self.sz+=1
	
			
	    #@end-editable@
        

    def insertFirst(self,u):
        #@start-editable@

		#creating a new node with given data
        nnode = self.node(u)

        
        #making head's value as u 
        if(self.isEmpty()):
            self.head = self.tail =nnode

        else:
            nnode.next = self.head
            self.head.prev = nnode
            self.head = nnode
        
        self.sz+=1
	
			
	    #@end-editable@
        
        
         
    #insert a node with value u after the node containing value v
    # error message: Node to insert after not found
    def insertAfter(self,u,v):
        #@start-editable@

		#create a new node
        nnode = self.node(u)

        #traverse to find node with element v
        if(not self.isEmpty()==0):
            if(self.size()==1 and (self.head.element==v)):
                self.insertLast(u)

            else:
                tnode = self.head
                flag = False

                while(tnode.next!=None and not flag):

                    if tnode.element!=v:
                    tnode=tnode.next

                else: 
                    flag = True

                #if such node exists, insert node after that
                if(flag):
                #procedure to insert node after tnode (check)
                    nnode.next=tnode.next
                    tnode.next=nnode
                    nnode.prev=tnode
                    tnode.next.prev=nnode
                self.sz+=1

        #else print error
            else:
                print("Node to insert after not found")
	
			
	    #@end-editable@
        return


    #insert a node with value u before the node containing value v
    # error message: Node to insert before not found
    def insertBefore(self,u,v):
        #@start-editable@

            #create a new node
        if(self.listEmpty()):
            print("Empty list")


        elif self.size()==1 and (self.head.element==v):    
            self.insertLast()

        else:
            #traverse to find node with element v
            nnode = self.node(u)
            tnode = self.head   
            flag = False

            while(tnode.next!=None and not flag):

                if tnode.element!=v:
                    tnode=tnode.next

                else: flag = True

        #if such node exists, insert node before that
            if(flag):
            #set tnode to point to previous node
                tnode=tnode.prev

            #procedure to insert node after tnode (check)
                nnode.next=tnode.next
                tnode.next=nnode
                nnode.prev=tnode
                tnode.next.prev=nnode
                self.sz+=1
            
            else:
                print("Node to insert before not found")
    
	    #@end-editable@
        

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
          

    #delete the node after the node containting value u
    # error message: Node to delete after not found
    def deleteAfter(self,u):
        #@start-editable@

		#create traversal node
        tnode = self.head

        #traverse till finding element u
        flag = False
        while(tnode.next!=None and not flag):
            if(tnode.element!=u):
                tnode = tnode.next

            else: flag = True

        if flag:
            #deleting tnode

            #setting tnode as next node (ie to be deleted node)
            tnode = tnode.next

            #making prev node point to next node
            tnode.pre.next=tnode.next

            #making next node's prev point to prev node
            tnode.next.prev = tnode.prev

            #deleting node 
            del tnode
            self.sz-=1

        else: #INSERT ERROR MESSAGE 
            print("Node to delete after not found")
	
			
	    #@end-editable@
        

    #delete the node before the node containting value u
    # error message: Node to delete before not found
    def deleteBefore(self,u):
        #@start-editable@

			#create traversal node 
        tnode = self.head

        #traverse 
        flag = False
        while(tnode.next!=None and not flag):
            if(tnode.element!=u):
                tnode=tnode.next

            else:
                flag=True

        if flag:

            if self.size()==1:
                return

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
        

    def findNode(self, val):
        #@start-editable@

		#create a node to traverse
        tnode = self.head

        #traverse
        flag = False
        while(tnode.next!=None and not flag):
            
            if(tnode.element!=val):
                tnode=tnode.next

            else: flag=True

        #if element exists, return it
        if(flag is True):
            return tnode
	
			
	    #@end-editable@
        

    #swap the nodes containing u and v
    def swap(self,u,v):
        #@start-editable@

        iterate_1 = self.head
        while iterate_1.next is not None:
            if iterate_1.element == u:
                break
            iterate_1 = iterate_1.next
        iterate_2 = self.head
        while iterate_2.next is not None:
            if iterate_2.element == v:
                break
            iterate_2 = iterate_2.next

        temp = iterate_1.element
        iterate_1.element = iterate_2.element
        iterate_2.element = temp
  
			
	    #@end-editable@
        
 
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