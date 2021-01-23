    class SLList:

        class node:
            def __init__(self,data):
                self.element = data
                self.next = None
        
        def __init__(self):
            self.head = self.node(None)
            self.sz = 0

            
        def insertLast(self,data):
            new_node = self.node(data)

            if self.isEmpty():
                self.head = new_node;
                self.sz+=1

            else:
                traversal = self.head

                while traversal.next!=None:
                    traversal = traversal.next

                traversal.next = new_node
                self.sz+=1

            return

        def insertFirst(self,data):
            new_node = self.node(data)

            if self.isEmpty():
                self.head = new_node;
                self.sz+=1

            else:
                new_node.next = self.head
                self.head = new_node
                self.sz+=1

            return

        def deleteFirst(self):
            if self.sz!=0:
                if self.head.next==None:
                    self.head.element = None

                else:
                    temp = self.head
                    self.head = self.head.next
                    del temp
                self.sz-=1

            return

        def deleteLast(self):
            if self.size()==0:
                if self.head.next==None:
                    self.head.element = None
                    
                else:
                    traversal = self.head

                    while traversal.next.next!=None:
                        traversal = traversal.next
                    
                    temp = traversal.next
                    traversal.next=None
                    del temp
                self.sz-=1

            return
            
        def isEmpty(self):
            return (self.sz==0)
            
        def size(self):
            return self.sz
            
                
        def printList(self):
            if (self.isEmpty()):
                print ("Linked List Empty Exception")
            else:
                tnode = self.head
            while tnode!= None:
                print(tnode.element,end=" ")
                tnode = tnode.next
            print(" ")
            return
        
        def findNode(self, val):
            
            return
            
        

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
            elif(operation[0]=="IF"):
                sll.insertFirst(int(operation[1]))
                sll.printList()
            elif(operation[0]=="IL"):
                sll.insertLast(int(operation[1]))
                sll.printList()
            elif(operation[0]=="DF"):
                sll.deleteFirst()
                sll.printList()
            elif(operation[0]=="DL"):
                sll.deleteLast()
                sll.printList()
        
            inputs-=1


def main():
    testSLL()

if __name__ == '__main__':
    main()
