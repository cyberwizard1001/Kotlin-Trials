class Node(object):
    def __init__(self,val):
        self.value = val
        self.leftchild = None
        self.rightchild = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def PreOrderTraversal(self,v):
        if v!=None:
            print(v.value,end=" ")
            self.PreOrderTraversal(self,v.leftchild)
            self.PreOrderTraversal(self,v.rightchild)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)




