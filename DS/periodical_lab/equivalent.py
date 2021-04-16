import math
from collections import deque

class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0


    def getChildren(self, curnode):
        children = []
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def isRoot(self,curnode):
    	if (curnode.parent==None):
    		return True
    	else:
    		return False

    def inorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderTraverse(curnode.leftchild)
        print (curnode.element,end = ",")
        if (curnode.rightchild != None):
            self.inorderTraverse(curnode.rightchild)

    def preorderTraverse(self, v):
        curnode = v
        print(curnode.element,end=",")
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.preorderTraverse(curnode.rightchild)
        

    def postorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.postorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.postorderTraverse(curnode.rightchild)
        print (curnode.element,end=",")
        

    def levelorderTraverse(self, v):
        q1 = deque()
        q1.append(v)
        while (len(q1)>0):
        	temp=q1.popleft()
        	print(temp.element,end=",")
        	if temp.leftchild!=None:
        		q1.append(temp.leftchild)
        	if temp.rightchild!=None:
        		q1.append(temp.rightchild)
        return



    def buildTree(self, expr):
        #@start-editable

        expr = expr.replace(" ","")
        i = 0
        flag = False

        while(i<len(expr) and flag==False):
            char = expr[i]

            if(char==")"):
                flag = True

            i+=1 

        i = i-1
        flag = False

        while(i>-1 and flag==False):
            char = expr[i]

            if(char=="("):
                flag = True

        



        nodelist = []
        nodelist.append(None)
        for i in range(len(expr)):
            if (i != 0):
                if (str[i] != -1) and (str[i]!=","):
                    tempnode = self.node()
                    tempnode.element = str[i]
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]
                        if (i % 2 == 0):
                            nodelist[i // 2].leftchild = tempnode
                        else:
                            nodelist[i // 2].rightchild = tempnode
                    nodelist.append(tempnode)
                elif str[i]==-1:
                    nodelist.append(None)
        
        self.root = nodelist[1]
        self.sz=len(nodelist)	
			
        #@end-editable@
        return nodelist
			
			
        #@end-editable@
        return nodelist

    # write a function to visualize the tree

    def equivalent(self, treevec1, root1, treevec2, root2):
        #@start-editable@



        #@end-editable@
        

    def printTree(self, nlist):
        for i in range(len(nlist)):
            print(nlist[i].element,end=" ")


    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz


def main():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    inputs = int(input())
    while (inputs > 0):
        exp1 = input()
        exptree1 = tree1.buildTree(exp1)
        tree1.printTree(exptree1)
        exp2 = input()
        exptree2 = tree2.buildTree(exp2)
        tree2.printTree(exptree2)
        print(tree1.equivalent(exptree1, tree1.root, exptree2, tree2.root))
        inputs -= 1
 
if __name__ == '__main__':
    main()