class SLList:

     class node:
         def __init__(self,data):
               self.element = data
               self.next = None
        
     def __init__(self):
          self.head = self.node(None)
          self.sz = 0
          
     def insertLast(self,data):

         return
          
     def insertFirst(self,data):

         return

         
     def deleteFirst(self):

         return


     def deleteLast(self):

         return
          
     def isEmpty(self):

         return
         
     def size(self):

         return
         
                
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
