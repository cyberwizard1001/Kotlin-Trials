def kth_node(self,k):
#delete every kth node
	node = self.head
	count = 0
	while(node.next!=None):	
		if(count%k==1)
			if(node.next.next!=None):
				node = node.next.next
				count+=1
				
			else return
	
		else
			node = node.next
			count+=1
			
			
def sorted_insert(self,data):
#sort the list as it's being udpated
	node = self.head
	
	if(self.size()==0):
		nnode = self.node(data) 
		self.head = nnode
	
	while(node.next!=None):	
		if(data<=node.element):
			node = node.next
		
		else:
			nnode = self.node(data)
			node.next.next = nnode.next
			node.next = nnode
			

def del_altk(self,k):
#delete k elements every kth element
	node = self.head
	count = 0
	while(node.next!=None):
		if(count%k==0):
			temp = node
			for i in range(1,k):
				temp = node.next
				node.next=node.next.next
				count+=1
			node = temp.next

		count+=1
