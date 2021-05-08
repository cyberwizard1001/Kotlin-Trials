class AvlTree:

    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, key):
            self.key = key
            self.leftchild = None
            self.rightchild = None
            self.height = 1

    def getHeight(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def leftRotate(self, node):
        right = node.rightchild
        rightsleft = right.leftchild

        right.leftchild = node
        node.rightchild = rightsleft

        node.height = 1 + max(self.getHeight(node.leftchild),self.getHeight(node.rightchild))
        right.height = 1 + max(self.getHeight(right.leftchild),self.getHeight(right.rightchild))

        return right

    def rightRotate(self, node):
        left = node.leftchild
        leftsright = left.rightchild

        left.leftchild = node
        node.rightchild = leftsright

        node.height = 1 + max(self.getHeight(node.leftchild),self.getHeight(node.rightchild))
        left.height = 1 + max(self.getHeight(left.leftchild),self.getHeight(left.rightchild))

    def getBalanceFactor(self, node):
        if node is None:
            return 0
        
        return self.getHeight(node.leftchild)-self.getHeight(node.rightchild)

    def insertElement(self, node, key):
        if node is None:
            return self.Node(key)

        elif key>node.key:
            node.rightchild = self.insertElement(node.rightchild,key)

        else:
            node.leftchild = self.insertElement(node.leftchild,key)

        node.height = 1 + max(self.getHeight(node.leftchild),self.getHeight(node.rightchild))
        bal_factor = self.getBalanceFactor(node)

        if bal_factor < -1 and key<node.leftchild.key:
        #(to identify left rotation)
            return self.leftRotate(node)

        if bal_factor > 1 and key<node.leftchild.key:
        #(to identify right rotation)
            return self.rightRotate(node)

        elif bal_factor>1 and key>node.leftchild.key:
            node.leftchild = self.leftRotate(node.leftchild)
            return self.rightRotate(node)
        
        elif bal_factor<-1 and key<node.rightchild.key:
            node.rightchild = self.rightRotate(node.rightchild)
            return self.leftRotate(node)

        return node


    def deleteElement(self, node, key):
        if node is None:
            return node

        elif key<node.key:
            node.leftchild = self.deleteElement(node.leftchild,key)
        elif key>node.key:
            node.leftchild = self.deleteElement(node.rightchild,key)
        else:
            if node.leftchild is None:
                temp = node.rightchild
                node = None 
                return temp 
            elif node.rightchild is None:
                temp = node.leftchild
                node = None
                return temp
            else:
                temp = node.rightchild
                while temp.leftchild is not None:
                    temp = temp.key
                node.key = temp.key
                node.rightchild = self.deleteElement(node.rightchild,temp.key)

            if node is None:
                return node

            node.height = 1 + max(self.getHeight(node.leftchild),self.getHeight(node.rightchild))
            bal_factor = self.getBalanceFactor(node)

            if bal_factor < -1 and self.getBalanceFactor(node.rightchild<=0):
            #(to identify left rotation)
                return self.leftRotate(node)

            if bal_factor > 1 and self.getBalanceFactor(node.leftchild)>=0:
            #(to identify right rotation)
                return self.rightRotate(node)

            elif bal_factor>1 and self.getBalanceFactor(node.leftchild)<0:
            #double rotation 1
                node.leftchild = self.leftRotate(node.leftchild)
                return self.rightRotate(node)
            
            elif bal_factor<-1 and self.getBalanceFactor(node.rightchild)>0:
            #double rotation 2
                node.rightchild = self.rightRotate(node.rightchild)
                return self.leftRotate(node)
            

    def preorder(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.preorder(root.leftchild)
        self.preorder(root.rightchild)

def main():
	tree = AvlTree()
	for i in range(int(input())):
		inp = input()
		if 'I' in inp:
			key = int(inp.split()[1])
			tree.root = tree.insertElement(tree.root, key) 
			tree.preorder(tree.root)
			print()
		elif 'D' in inp:
			key = int(inp.split()[1])
			tree.root = tree.deleteElement(tree.root, key) 
			tree.preorder(tree.root)
			print()

if __name__ == '__main__':
	main()