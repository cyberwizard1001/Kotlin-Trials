class DeckRemove:
    #@start-editable@

    def __init__(self):
        self.dck = DLList()
        self.tmp = [10,20,30]
        


    def insertInto(self,deck1,x):
        self.j = 0
        while(self.i < len(deck1) and self.j < x):
            if(deck1[self.i] == "K" or deck1[self.i] == "Q" or deck1[self.i] == "J"):
                self.dck.insertLast(10)
            elif (deck1[self.i] == "A"):
                self.dck.insertLast(1)
            else:
                self.dck.insertLast(int(deck1[self.i]))
            self.i += 1
            self.j += 1
        
	
	#@end-editable@

    def checkDeck(self, deck1):
    
    #@start-editable@
        self.total = 0
        self.s4 = 0
        self.i = 0
        self.insertInto(deck1,7)

        while(self.i <=  len(deck1) and self.dck.size() > 3):

            self.s1 = self.dck.getHead().element + self.dck.getHead().next.element + self.dck.getLastNode().element
            self.s2 = self.dck.getHead().element + self.dck.getLastNode().element + self.dck.getLastNode().prev.element
            self.s3 = self.dck.getLastNode().element + self.dck.getLastNode().prev.element + self.dck.getLastNode().prev.prev.element

            if(self.s1 in self.tmp):
                self.total += self.s1
                self.dck.deleteFirst()
                self.dck.deleteFirst()
                self.dck.deleteLast()

            elif(self.s2 in self.tmp):
                self.total += self.s2
                self.dck.deleteFirst()
                self.dck.deleteLast()
                self.dck.deleteLast()

            elif(self.s3 in self.tmp):
                self.total += self.s3
                self.dck.deleteLast()
                self.dck.deleteLast()
                self.dck.deleteLast()
            
            else:
                break
        
            if(self.i <= len(deck1)):
                self.insertInto(deck1,3)

        if(self.dck.size() > 0 and self.dck.size() <= 3):
            self.node = self.dck.getHead()

            while(self.node != None):
                self.s4 += self.node.element
                self.node = self.node.next
        
            if(self.s4 in self.tmp):
                self.total += self.s4
                while(self.dck.size() > 0):
                    self.dck.deleteFirst()
        
        if(self.dck.isEmpty()):
            self.emt = True
        else:
            self.emt = False

        print("{emt} {total}".format(emt = self.emt,total = self.total))
        
			
			
	#@end-editable@   