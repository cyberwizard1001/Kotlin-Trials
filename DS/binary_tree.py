import math
from collections import deque

class BinaryTree:
    class node:
        def __init_(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0

    def getChildren(self,curnode):
        children = []
        if curnode.leftchild!=None:
            children.append(curnode.leftchild)
        if curnode.rightchild!=None:
            children.append(curnode.rightchild)
        return children
        